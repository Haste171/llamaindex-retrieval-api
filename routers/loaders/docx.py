import tempfile, os
from routers.utils.engine import Engine
from pathlib import Path
from llama_index import download_loader
from fastapi import APIRouter, UploadFile, HTTPException

engine = Engine()
router = APIRouter()

@router.post("/docx")
async def file(upload_file: UploadFile, namespace: str):
    """
    Loader: https://llamahub.ai/l/file-docx
    """
    file_preview_name, file_extension = os.path.splitext(upload_file.filename)
    if file_extension != '.docx':
        raise HTTPException(status_code=400, detail="File must be a docx")
    
    with tempfile.NamedTemporaryFile(delete=True, prefix=file_preview_name + '_', suffix=".docx") as temp_file:
        content = await upload_file.read()
        temp_file.write(content)
        DocxReader = download_loader("DocxReader")
        loader = DocxReader().load_data(file=Path(temp_file.name))
        engine.load(loader, namespace)
    
    return {'message': 'File uploaded successfully', 'filename': upload_file.filename, "namespace": namespace}