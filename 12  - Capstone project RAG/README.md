# Customer Support Chatbot

Данный проект представляет собой чат-бот для обслуживания клиентов, который позволяет:
1. Отвечать на вопросы пользователей на основе загруженных документов (PDF, TXT и т. п.).
2. При отсутствии найденного ответа, а также по желанию пользователя, создавать тикеты (issues) в GitHub.

## Структура проекта

.
├─ data/                     # Документы для индексации
│   ├─ manual_1.pdf         # Минимум 400+ страниц
│   ├─ manual_2.pdf
│   └─ some_doc.txt         # Пример текстового документа
├─ faiss_index/             # Папка, где хранится индекс (FAISS)
│   ├─ index
│   └─ index.pkl
├─ .env                     # Секретные переменные (не кладите в публичный репозиторий!)
├─ requirements.txt         # Зависимости проекта
├─ index_data.py            # Скрипт для индексации данных (PDF/TXT) и создания векторного индекса
├─ github_issue.py          # Модуль для создания GitHub Issue
├─ app.py                   # Основной файл Streamlit-приложения
└─ README.md                # Текущее описание проекта


## Возможности

- **Поиск и ответы** на основе локальных документов (минимум 3, включая хотя бы 2 PDF, один из которых более 400 страниц).
- **История диалога** — хранение контекста вопросов и ответов.
- **Создание тикетов (Issue) в GitHub**, если ответ не найден или пользователь этого хочет.
- **Цитирование** источников (указывается имя файла, страница и пр.).

## Установка

1. **Клонируйте репозиторий** (или скачайте архив):
   ```bash
   git clone https://github.com/aliaksei-babuk/masters-ai-aliaksei-babuk.git
   cd masters-ai-aliaksei-babuk

2.  **Установите зависимости**:  
    pip install -r requirements.txt

3. **Подготовка данных**
Поместите документы в папку data/.

Требуется как минимум 3 файла (2 PDF и 1 любой другой), при этом один PDF должен иметь 400+ страниц.

4. **Индексация документов**
Запустите скрипт:
    ``` bash
    python index_data.py

Скрипт проанализирует PDF/тексты из data/, разобьёт их на фрагменты, создаст эмбеддинги и сохранит всё это в FAISS (папка faiss_index/).

5. **Запуск чат-бота**
Убедитесь, что у вас активировано виртуальное окружение с установленными зависимостями.

Выполните команду:
    ``` bash
    streamlit run app.py
    
Откройте адрес, указанный в консоли (обычно http://localhost:8501).
## Created GitHub issue
https://github.com/aliaksei-babuk/masters-ai-aliaksei-babuk/issues
## UI works examples
![image](https://github.com/aliaksei-babuk/masters-ai-aliaksei-babuk/blob/main/12%20%20-%20Capstone%20project%20RAG/1.png) 
![image](https://github.com/aliaksei-babuk/masters-ai-aliaksei-babuk/blob/main/12%20%20-%20Capstone%20project%20RAG/3.png) 
Локально получилось запустить на Hugging face вышле нестыковка версий пакетов пока не знаю как ее решить
## Hugging face
https://huggingface.co/spaces/AliakseiBabuk/masters-ai-aliaksei-babuk