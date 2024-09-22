from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import List
from pydantic import BaseModel
from app.api.models import PredictionResponse
from app.services.emotion_service import batch_predict_emotions

router = APIRouter(
    tags=["Prediction"],
)

@router.post("/batch_predict/")
async def batch_predict(files: List[UploadFile] = File(...)):
    try:
        results = await batch_predict_emotions(files)
        prediction_responses = [PredictionResponse(emotion=pred['emotion'], confidence=pred['confidence']) for pred in results]
        return prediction_responses
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


