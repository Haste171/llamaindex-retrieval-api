# retrieval-api
 Retrieval API that utilizes llama-index 

# Installation
`pip install -r requirements.txt`

# Startup
`uvicorn main:app --reload`

# Access
http://localhost:8000/docs

# Loaders
`PDF` `DOCX` `IPYNB`

# TODO
- Add API endpoint for chatting with content (chat history etc.) ref. https://gpt-index.readthedocs.io/en/stable/core_modules/query_modules/chat_engines/usage_pattern.html
- Add more loaders
- Create dynamic loader for files (one endpoint)