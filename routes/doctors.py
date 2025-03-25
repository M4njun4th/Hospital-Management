from fastapi import APIRouter, HTTPException
from models import Doctor
from database import db
import shortuuid  

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.post("/")
async def add_doctor(doctor: Doctor):
    doctor_dict = doctor.model_dump()  
    
    #Generated a short unique ID of length 6
    short_id = shortuuid.uuid()[0:6]
    doctor_dict["_id"] = short_id  
    #inserting to doctors collection
    new_doctor = await db.doctors.insert_one(doctor_dict)
    return {"id": str(new_doctor.inserted_id)}

@router.get("/{doctor_id}")
async def get_doctor(doctor_id: str):
    doctor = await db.doctors.find_one({"_id":(doctor_id)})
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor
