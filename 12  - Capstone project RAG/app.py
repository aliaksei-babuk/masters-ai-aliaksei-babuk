from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import faiss
import time
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage
from github_issue import create_github_issue
import openai

# Set OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
github_repo_owner = os.getenv("GITHUB_REPO_OWNER")
github_repo_name = os.getenv("GITHUB_REPO_NAME")
github_token = os.getenv("GITHUB_PAT_TOKEN")

def load_vectorstore(faiss_index_path):
    embeddings = OpenAIEmbeddings(
        openai_api_key=openai_api_key
    )
    vectorstore = FAISS.load_local(
        faiss_index_path,
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vectorstore

def cite_source(page_content, metadata):
    # Простейший вариант генерации "цитаты" – укажем имя файла и (если есть) номер страницы
    source_file = metadata.get("source_file", "unknown_file")
    page = metadata.get("page", None)
    if page:
        return f"Источник: {source_file}, страница {page}"
    else:
        return f"Источник: {source_file}"

def generate_answer(question, vectorstore, conversation_history):
    llm = ChatOpenAI(
        model_name="gpt-4",
        openai_api_key=openai_api_key,
        temperature=0
    )
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
        output_key="answer"
    )

    # "Запускаем" chain
    result = qa_chain({"question": question, "chat_history": conversation_history})
    answer_text = result["answer"]

    # Извлекаем актуализированную историю
    updated_history = memory.load_memory_variables({})["chat_history"]
    return answer_text, updated_history

def main():
    st.title("Customer Support Chatbot")
    st.write("Добро пожаловать в систему поддержки! Компания: Azure Well Architectured Advisor. Пожалуйста используйте форму ниже для создания запросов по WAF, телефон: +1-202-555-0123, email: support@example.com")

    if "conversation_history" not in st.session_state:
        st.session_state["conversation_history"] = []

    # Загрузка векторного хранилища (FAISS)
    vectorstore = load_vectorstore("faiss_index")

    # Блок вопрос-ответ
    st.header("Задайте вопрос")
    user_question = st.text_input("Введите ваш вопрос:")

    if st.button("Спросить"):
        if user_question.strip():
            answer, updated_history = generate_answer(
                user_question,
                vectorstore,
                st.session_state["conversation_history"]
            )
            st.session_state["conversation_history"] = updated_history
            st.write("**Ответ:**")
            st.write(answer)

            # Условная логика: если ответ кажется пустым или указывает, что ответа нет,
            # можно предложить оформить тикет (но это необязательно).
            if "не знаю" in answer.lower() or "не нашлось" in answer.lower():
                st.warning("Похоже, точный ответ не найден. Вы можете оформить тикет на доработку.")
        else:
            st.info("Сначала введите вопрос.")

    st.write("---")
    st.header("Опционально: создать тикет в GitHub")
    st.write("Если у вас остались вопросы или требуется поддержка — создайте тикет.")
    # Создаем форму
    with st.form("ticket_form"):
        st.write("Введите данные для тикета:")
        user_name = st.text_input("Ваше имя:")
        user_email = st.text_input("Ваш email:")
        ticket_description = st.text_area("Опишите проблему или запрос подробно:")

        # Кнопка формы
        submitted = st.form_submit_button("Подтвердить создание тикета")
        if submitted:
            title = f"Вопрос от {user_name}"
            body = f"Email: {user_email}\n\nОписание:\n{ticket_description}"
            issue_url = create_github_issue(
                repo_owner=github_repo_owner,
                repo_name=github_repo_name,
                token=github_token,
                title=title,
                body=body
            )
            st.success(f"Тикет создан! Ссылка: {issue_url}")

    # Отображаем историю чата (упрощённо)
    if st.session_state["conversation_history"]:
        st.write("---")
        st.write("## История диалога :")
        for idx, msg in enumerate(st.session_state["conversation_history"]):
            # Проверяем класс сообщения
            if isinstance(msg, HumanMessage):
                role_str = "Human"
            elif isinstance(msg, AIMessage):
                role_str = "AI"
            else:
                role_str = "System"  # или любой другой вариант
            
            st.write(f"{idx+1}. {role_str} сказал(а): {msg.content}")

if __name__ == "__main__":
    main()
