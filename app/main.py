from fastapi import FastAPI
from app.routes.process import router as process_router

app = FastAPI()

app.include_router(process_router)

@app.get("/")
def home():
    return {"message": "Claim Processor API Running"}