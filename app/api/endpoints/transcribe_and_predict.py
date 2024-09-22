from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import List
from pydantic import BaseModel
from app.api.models import PredictionResponse
from app.services.emotion_service import transcribe_and_predict

router = APIRouter(
    tags=["Prediction"],
)

class TranscriptionResponse(BaseModel):
    transcription: str
    emotion: str
    confidence: float

@router.post("/transcribe_and_predict/", response_model=TranscriptionResponse)
async def transcribe_and_predict_endpoint(file: UploadFile = File(...)):
    try:
        transcription, emotion, confidence = await transcribe_and_predict(file)
        return TranscriptionResponse(transcription=transcription, emotion=emotion, confidence=confidence)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
