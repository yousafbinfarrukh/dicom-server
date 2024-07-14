from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship
import enum
from datetime import datetime

class UserRole(str, enum.Enum):
    patient = "patient"
    admin = "admin"
    technician = "technician"
    doctor = "doctor"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(UserRole))

class DICOMFile(Base):
    __tablename__ = "dicom_files"

    id = Column(Integer, primary_key=True, index=True)
    file_path = Column(String, unique=True, index=True)
    upload_time = Column(DateTime, default=datetime.utcnow)
    patient_id = Column(String)
    study_id = Column(String)
    modality = Column(String)
    institution_name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User")
