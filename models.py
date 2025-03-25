from pydantic import BaseModel, EmailStr      
from datetime import datetime, timezone

#User Authentication Model
class User(BaseModel):  #to validate input data
    email: EmailStr
    password: str

#Patient model
class Patient(BaseModel):
    name: str
    age: int
    gender: str
    contact: str
    address: str

#Doctor Model
class Doctor(BaseModel):
    name: str
    specialization: str
    contact: str

#Consultation Model
class Consultation(BaseModel):
    patient_id: str
    doctor_id:str
    diagnosis: str
    prescription: str
    date: datetime = datetime.now(timezone.utc)
