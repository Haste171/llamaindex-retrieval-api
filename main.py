from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    'http://localhost:3000'
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

from routers.router import app as app_router
app.include_router(app_router)