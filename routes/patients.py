from fastapi import APIRouter, HTTPException, Query
from models import Patient
from database import db
import shortuuid 

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post("/add-patient")
async def add_patient(patient: Patient):
    patient_dict = patient.model_dump()

    # Generate a short unique ID using shortuuid
    short_id = shortuuid.uuid()[0:6]
    
    # Assign short ID to _id so MongoDB uses it as the primary key
    patient_dict["_id"] = short_id

    print("Adding new patient:", patient_dict)  

    # Save to database
    await db.patients.insert_one(patient_dict)

    return {"id": short_id}


@router.get("/get-patient")
async def get_patient(patient_id: str = Query(..., title="Patient ID")):
    print(f"Fetching patient with ID: {patient_id}") 

    patient = await db.patients.find_one({"_id": patient_id})

    if not patient:
        print(f"No patient found with ID: {patient_id}")
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient
