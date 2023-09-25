import tempfile, os
from routers.utils.engine import Engine
from pathlib import Path
from llama_index import download_loader
from fastapi import APIRouter, UploadFile, HTTPException

engine = Engine()
router = APIRouter()

@router.post("/ipynb")
async def file(upload_file: UploadFile, namespace: str):
    """
    Loader: https://llamahub.ai/l/file-ipynb
    """
    file_preview_name, file_extension = os.path.splitext(upload_file.filename)
    if file_extension != '.ipynb':
        raise HTTPException(status_code=400, detail="File must be a IPynb")
    
    with tempfile.NamedTemporaryFile(delete=True, prefix=file_preview_name + '_', suffix=".ipynb") as temp_file:
        content = await upload_file.read()
        temp_file.write(content)
        IPYNBReader = download_loader("IPYNBReader")
        loader = IPYNBReader(concatenate=True).load_data(file=Path(temp_file.name))
        engine.load(loader, namespace)
    
    return {'message': 'File uploaded successfully', 'filename': upload_file.filename, "namespace": namespace}