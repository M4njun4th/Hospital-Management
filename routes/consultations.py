from fastapi import APIRouter, HTTPException
from models import Consultation
from database import db
import shortuuid

router = APIRouter(prefix="/consultations", tags=["Consultations"])

@router.post("/")
async def add_consultation(consultation: Consultation):
    consultation_dict = consultation.model_dump()

    # Generated a 6-character ID
    short_id = shortuuid.uuid()[0:6]
    consultation_dict["_id"] = short_id 

    # Inserting to table
    await db.consultations.insert_one(consultation_dict)
    return {"id": short_id}

@router.get("/{consultation_id}")
async def get_consultation(consultation_id: str):

    # Fetching consultation using consultation id
    consultation = await db.consultations.find_one({"consultation_id": consultation_id})
    if not consultation:
        raise HTTPException(status_code=404, detail="Consultation not found")

    return consultation 
