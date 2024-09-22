from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.services.emotion_service import predict_emotion
from app.api.models import PredictionResponse

router = APIRouter(
    tags=["Prediction"],
)

@router.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    try:
        emotion, confidence = await predict_emotion(file)
        return PredictionResponse(emotion=emotion[0], confidence=confidence)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
