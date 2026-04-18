from unittest import result

from fastapi import APIRouter, UploadFile, File, Form
from app.services.pdf_loader import extract_pages
from app.services.segregator import classify_pages
from app.services.id_agent import extract_identity
from app.services.discharge_agent import extract_discharge
from app.services.bill_agent import extract_bill
from app.graph.workflow import build_graph

router = APIRouter(prefix="/api")

graph = build_graph()

@router.post("/process")
async def process_claim(
    claim_id: str = Form(...),
    file: UploadFile = File(...)
):
     result = graph.invoke({
        "claim_id": claim_id,
        "file": file
    })
     return result["result"]