from fastapi import FastAPI
from database import db 
from routes import auth, patients, doctors, consultations

routes = FastAPI()

# Including Routes
routes.include_router(auth.router)
routes.include_router(patients.router)
routes.include_router(doctors.router)
routes.include_router(consultations.router)

@routes.get("/")
async def root():
    return {"message": "Hospital Management API"}
