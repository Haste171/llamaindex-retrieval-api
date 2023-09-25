from .retrievers import query
from .loaders import pdf, docx
from fastapi import APIRouter

app = APIRouter()

app.include_router(query.router, tags=["retrieval"], prefix='/retrieval')
app.include_router(pdf.router, tags=["load"], prefix='/load')
app.include_router(docx.router, tags=["load"], prefix='/load')