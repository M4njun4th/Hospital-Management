
## **Hospital Management API**

This is a basic yet impactful Hospital Management API that is constructed with FastAPI and MongoDB to manage patients, doctors, and consultations with efficiency. It achieves safe user password authentication through the use of bcrypt, and rather than using traditional ObjectIDs, the API uses short UUIDs to keep the database structure cleaner. The API's modularity design is aimed at making it easier to scale and maintain. In addition to Motor’s asynchronous database operations being used, one can have fast and reliable performance. If one is to input a new patient, a doctor's personal data or the consultation records, the system will give the ease in hospital data management.

---

## **Features**
- **User Authentication** (Signup & Login)
- **Patient Management** (Add & Retrieve Patients)
- **Doctor Management** (Add & Retrieve Doctors)
- **Consultations** (Add & Retrieve Consultations)
- **Password Hashing** using bcrypt
- **MongoDB Integration** with `motor`
- **Short UUIDs** instead of ObjectId for better readability

---



