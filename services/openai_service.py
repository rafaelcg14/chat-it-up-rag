from openai import AzureOpenAI
import os
from dotenv import load_dotenv
import re

# Load environment variables
load_dotenv()
azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
azure_oai_key = os.getenv("AZURE_OAI_KEY")
azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
azure_oai_version = os.getenv("AZURE_OAI_VERSION")
search_endpoint =  os.getenv("AZURE_SEARCH_ENDPOINT")
search_key = os.getenv("AZURE_SEARCH_KEY")
search_index = os.getenv("AZURE_SEARCH_INDEX_NAME")
semantic_config = os.getenv("AZURE_SEARCH_SEMANTIC_CONFIG")

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=azure_oai_endpoint,
    api_key=azure_oai_key,
    api_version=azure_oai_version
)

# Global conversation history
conversation_history = [
    {
        "role": "system",
        "content": "You are an AI assistant that helps people find information only from the retrieved documents."
    }
]

async def chat_with_openai( message: str ) -> str:
    # Append the new user message to the conversation history
    conversation_history.append({"role": "user", "content": message})

    # Integration with Azure AI Search
    extra_body = {
        "data_sources": [{
            "type": "azure_search",
            "parameters": {
                "endpoint": f"{search_endpoint}",
                "index_name": "vector-1731459204776",
                "semantic_configuration": "vector-1731459204776-semantic-configuration",
                "query_type": "vector_semantic_hybrid",
                "fields_mapping": {},
                "in_scope": True,
                "role_information": "You are an AI assistant that helps people find information only in the retrieved documents.",
                "filter": None,
                "strictness": 3,
                "top_n_documents": 5,
                "authentication": {
                "type": "api_key",
                "key": f"{search_key}"
                },
                "embedding_dependency": {
                    "type": "deployment_name",
                    "deployment_name": "text-embedding-ada-002"
                }
            }
        }]
    }

    # Send the conversation history to OpenAI
    response = client.chat.completions.create(
        model=azure_oai_deployment,
        messages=conversation_history,
        max_tokens=800,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False,
        extra_body=extra_body
    )

    # Get the assistant's response
    chat_response = response.choices[0].message.content

    # Remove [doc1], [doc2], etc., from chat_response
    chat_response_cleaned = re.sub(r"\s*\[doc\d+\]\s*", " ", chat_response)
    chat_response_cleaned = re.sub(r"\s+", " ", chat_response_cleaned).strip()

    # Append the assistant's response to the conversation history
    conversation_history.append({"role": "assistant", "content": chat_response_cleaned})
    
    # Get the reference titles
    reference_titles = set()
    citations_list = response.choices[0].message.context['citations']
    
    for citation in citations_list:
        title = citation['title']
        if title:
            reference_titles.add( title )

    reference_titles = list(reference_titles)

    return {
        "chat_response": chat_response_cleaned,
        "reference_titles": reference_titles
    }
    