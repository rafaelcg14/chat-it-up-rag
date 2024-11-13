import os
from azure.search.documents.indexes import SearchIndexerClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Setting up Azure resources keys
load_dotenv()

# Azure Cognitive Search configuration
azure_search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
azure_search_api_key = os.getenv("AZURE_SEARCH_KEY")
indexer_name = os.getenv("AZURE_SEARCH_INDEXER_NAME")

# Reset and run the indexer
def reset_and_run_indexer():
    indexer_client = SearchIndexerClient(
        endpoint=azure_search_endpoint,
        credential=AzureKeyCredential(azure_search_api_key)
    )
    try:
        # Reset the indexer
        indexer_client.reset_indexer(indexer_name)

        # Rerun the indexer
        indexer_client.run_indexer(indexer_name)
        
    except Exception as e:
        return {'status': 'error', 'message': str(e)}