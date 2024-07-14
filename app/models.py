from sqlalchemy import Column, Integer, String, Enum
from .database import Base
import enum

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
