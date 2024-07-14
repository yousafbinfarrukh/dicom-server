from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username, hashed_password=fake_hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_dicom_file(db: Session, dicom_file: schemas.DICOMFileCreate):
    db_dicom = models.DICOMFile(**dicom_file.dict())
    db.add(db_dicom)
    db.commit()
    db.refresh(db_dicom)
    return db_dicom
