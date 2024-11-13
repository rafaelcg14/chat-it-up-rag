from fastapi import APIRouter, UploadFile, File, HTTPException
from services.blob_storage_service import upload_file_to_blob
from services.search_service import reset_and_run_indexer
from typing import List

router = APIRouter()

@router.post('/upload-files')
async def upload_files( files: List[UploadFile] = File(...) ):
    try:
        for file in files:
            # Upload files to blob storage
            upload_file_to_blob( file )
        
        # Rerun the indexer
        reset_and_run_indexer()

        return { 'status': 'success' }
    except Exception as e:
        raise HTTPException( status_code=500, detail=str(e) )