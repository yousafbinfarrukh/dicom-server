from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
import os
import pydicom
from sqlalchemy.orm import Session
from .. import database, models, schemas, auth, crud
from datetime import datetime

router = APIRouter()

UPLOAD_FOLDER = '/home/yousaf/'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@router.post("/upload_dicom/", response_model=schemas.DICOMFile)
async def upload_dicom(file: UploadFile = File(...), db: Session = Depends(database.get_db), current_user: schemas.User = Depends(auth.get_current_active_user)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    dicom_data = pydicom.dcmread(file_path)
    metadata = {
        "file_path": file_path,
        "patient_id": dicom_data.PatientID,
        "study_id": dicom_data.StudyID,
        "modality": dicom_data.Modality,
        "institution_name": dicom_data.InstitutionName,
        "user_id": current_user.id
    }

    dicom_file = schemas.DICOMFileCreate(**metadata)
    return crud.create_dicom_file(db=db, dicom_file=dicom_file)
