from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from fastapi.responses import FileResponse
import os
import pydicom
from sqlalchemy.orm import Session
from .. import database, models, schemas, crud
from datetime import datetime

router = APIRouter()

UPLOAD_FOLDER = '/home/yousaf/dicoms/'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@router.post("/upload_dicom/", response_model=schemas.DICOMFile)
async def upload_dicom(file: UploadFile = File(...), db: Session = Depends(database.get_db)):
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
        "user_id": 1  # Set a default user_id for now
    }

    dicom_file = schemas.DICOMFileCreate(**metadata)
    return crud.create_dicom_file(db=db, dicom_file=dicom_file)

@router.get("/download_dicom/{dicom_id}")
def download_dicom(dicom_id: int, db: Session = Depends(database.get_db)):
    dicom_file = db.query(models.DICOMFile).filter(models.DICOMFile.id == dicom_id).first()
    if not dicom_file:
        raise HTTPException(status_code=404, detail="DICOM file not found")
    
    return FileResponse(dicom_file.file_path, media_type='application/dicom', filename=os.path.basename(dicom_file.file_path))
