from dotenv import load_dotenv
load_dotenv()
import os
import faiss
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import openai

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def index_documents(data_folder: str, faiss_index_path: str):
    # 1) Инициализируем объект для эмбеддингов
    embeddings = OpenAIEmbeddings(openai_api_key="OPENAI_API_KEY")

    all_docs = []

    # 2) Проходимся по PDF-файлам
    pdf_files = ["manual_1.pdf", "manual_2.pdf"]
    for pdf_file in pdf_files:
        loader = PyPDFLoader(os.path.join(data_folder, pdf_file))
        pdf_docs = loader.load_and_split()
        # В meta добавим имя файла, чтобы позже указывать при цитировании
        for d in pdf_docs:
            d.metadata["source_file"] = pdf_file
        all_docs.extend(pdf_docs)

    # 3) Загрузим дополнительный документ (TXT, DOCX и т.д.)
    text_file = "some_doc.txt"
    txt_loader = TextLoader(os.path.join(data_folder, text_file), encoding="utf-8")
    txt_docs = txt_loader.load_and_split()
    for d in txt_docs:
        d.metadata["source_file"] = text_file
    all_docs.extend(txt_docs)

    # 4) Применим дополнительный текстовый сплиттер для удобства
    #    (Если документы большие, это может быть особенно полезно)
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    splitted_docs = splitter.split_documents(all_docs)

    # 5) Создаём векторное хранилище FAISS
    vectorstore = FAISS.from_documents(splitted_docs, embeddings)

    # 6) Сохраняем локально
    vectorstore.save_local(faiss_index_path)

if __name__ == "__main__":
    # Пути в вашем проекте
    data_folder = "data"
    faiss_index_path = "faiss_index"
    index_documents(data_folder, faiss_index_path)
    print("Индексация завершена.")
