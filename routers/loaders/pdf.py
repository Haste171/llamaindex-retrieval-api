import tempfile, os
from routers.retrievers.utils.engine import Engine
from llama_index import download_loader
from fastapi import APIRouter, UploadFile, HTTPException

engine = Engine()
router = APIRouter()

@router.post("/pdf")
async def file(upload_file: UploadFile, namespace: str):
    """
    Loader: https://llamahub.ai/l/file-pymu_pdf
    """
    file_preview_name, file_extension = os.path.splitext(upload_file.filename)
    if file_extension != '.pdf':
        raise HTTPException(status_code=400, detail="File must be a PDF")
    
    with tempfile.NamedTemporaryFile(delete=True, prefix=file_preview_name + '_', suffix=".pdf") as temp_file:
        content = await upload_file.read()
        temp_file.write(content)
        PyMuPDFReader = download_loader("PyMuPDFReader")
        loader = PyMuPDFReader().load(file_path=temp_file.name, metadata=True)
        engine.load(loader, namespace)
    
    return {'message': 'File uploaded successfully', 'filename': upload_file.filename, "namespace": namespace}