# Chat It Up (Backend)

![Python Version](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.3-green)
![Azure OpenAI](https://img.shields.io/badge/Azure%20OpenAI-Enabled-blueviolet)
![Azure Blob Storage](https://img.shields.io/badge/Azure%20Blob%20Storage-Integrated-orange)
![Azure AI Search](https://img.shields.io/badge/Azure%20AI%20Search-Configured-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

This backend is part of a **Retrieval-Augmented Generation (RAG)** system that integrates **Azure OpenAI**, **Azure Blob Storage**, and **Azure AI Search** for intelligent document-based interactions. It allows users to upload files, store them in Azure Blob Storage, and index the documents for retrieval by the chatbot.

It is intended for **local use only** and was created as part of a Microsoft Innovation Challenge Hackathon. **Not for commercial use**.

![image](https://res.cloudinary.com/dtzfvm1m9/image/upload/v1731435967/portfolio/chat-it-up/tskxuei2bf8vrefeivtl.jpg)

---

## 🚀 Features
- **File Upload**: Save documents to Azure Blob Storage.
- **Azure AI Search**: Automatically trigger an Azure AI Search indexer for the uploaded files.
- **RAG Implementation**: Leverage Azure OpenAI's `gpt-35-turbo` for intelligent responses using indexed documents.

---

## ⚙️ Setup

### Prerequisites
1. **Python**: Version 3.10 or higher.
2. **Azure Resources**:
   - Azure OpenAI with a deployed GPT model (e.g., `gpt-35-turbo`) and a embedding model (e.g., `text-embedding-ada-002`).
   - Azure Blob Storage with a `docs` container (container access enabled).
   - Azure AI Search configured.
3. **Postman or cURL**: For API testing.

### Installation
For running this project in your local machine, you may run the following commands in your favorite prompt:

1. **Clone the Repository**:  
    ```bash
    git clone <repository_url>
    cd Chat-It-Up
2. **Set Up Virtual Environment**
    ```bash
    pip install virtualenv
    virtualenv .venv
3. **Activate Virtual Environment**
    
    Windows PowerShell:
    ```bash
    .venv\Scripts\activate
    ```
    
    Mac/Linux:
    ```bash
    source .venv/bin/activate
    ```

    Git Bash:
    ```bash
    .venv\Scripts\. activate
    ```
4. **Install Dependecies**
    ```bash
    pip install -r requirements.txt
5. **Configure Environment Variables**
    
    Create a `.env` file in the project root with the following variables:
    ```env
    AZURE_OAI_KEY=<your_openai_key>
    AZURE_OAI_ENDPOINT=<your_openai_endpoint>
    AZURE_OAI_VERSION=<your_openai_version>
    AZURE_OAI_DEPLOYMENT=<your_openai_model>

    AZURE_BLOB_CONNECTION_STRING=<your_blob_connection_string>
    AZURE_BLOB_CONTAINER_NAME=<your_container_name>

    AZURE_SEARCH_ENDPOINT=<your_search_endpoint>
    AZURE_SEARCH_KEY=<your_search_key>
    AZURE_SEARCH_INDEX=<your_search_index_name>
    AZURE_SEARCH_INDEXER_NAME=<your_search_indexer_name>
    AZURE_SEARCH_SEMANTIC_CONFIG=<your_search_semantic_configuration>
    ```
> **_NOTE:_**
> - Theses environment variables may be found in the code provided by the RAG deployment in Azure AI Studio as well.
> - It may occur an error while loading the Azure AI Search environment variables in the `openai_service.py`. If that occurs, insert the `AZURE_SEARCH_INDEX` and `AZURE_SEARCH_SEMANTIC_CONFIG` explicitly in that service file.

---

## 🛠️ Usage

### Running the Backend
Start the FastAPI server:

```bash
uvicorn main:app --reload
```

### API Endpoints
Test the chatbot using **cURL**:

```bash
curl -X POST "http://127.0.0.1:8000/files/upload-files" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "files=@<path_to_file>"
```

Test the file uploader using **Postman**:
1. URL: `http://localhost:8000/files/upload-files`
2. Method: `POST`
3. Configuration of the **body**: `form-data`
    
    | Key      | Value |
    | ----------- | ----------- |
    | File (*Files*)      | <your_selected_local_file>       |

Test the chatbot using **Postman**:
1. URL: `http://127.0.0.1:8000/chat`
2. Method: `POST`
3. Body/Raw/JSON:
    ```json
    {
    "message": "<your_message>"
    }
    ```
---

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## ⚠️ Disclaimer
This project was developed as part of a Microsoft Hackathon. It is designed for **educational and personal use only** and is not intended for production or commercial purposes.

### Participants
This project was developed by a passionate team of programming and AI enthusiasts. For more information about each team member, visit their profiles:

- Rafael Castellanos
    - [Portfolio](https://rafaelcg14.github.io/rafael-castellanos-portfolio/)
    - [GitHub](https://github.com/rafaelcg14)
    - [LinkedIn](https://www.linkedin.com/in/rafael-castellanos-guzman/)
- Samuel Díaz
    - [Portfolio](https://www.samuraidev.engineer/)
    - [GitHub](https://github.com/CodeGeekR)
    - [LinkedIn](https://www.linkedin.com/in/samuraidev/)

---

## Front-End Repository

- [Chat It Up!](https://github.com/rafaelcg14/chat-it-up-hackathon)

---

## 📚 Additional Documentation
- [Azure Open AI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Azure Blob Storage Documentation](https://learn.microsoft.com/en-us/azure/storage/blobs/)
- [Azure AI Search Documentation](https://learn.microsoft.com/en-us/azure/search/)
- [Fast API Documentation](https://fastapi.tiangolo.com/)