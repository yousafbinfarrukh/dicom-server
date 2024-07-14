from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class UserRole(str, Enum):
    patient = "patient"
    admin = "admin"
    technician = "technician"
    doctor = "doctor"

class UserBase(BaseModel):
    username: str
    role: UserRole

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class DICOMFileBase(BaseModel):
    file_path: str
    patient_id: str
    study_id: str
    modality: str
    institution_name: str
    user_id: int

class DICOMFileCreate(DICOMFileBase):
    pass

class DICOMFile(DICOMFileBase):
    id: int
    upload_time: datetime

    class Config:
        orm_mode = True
