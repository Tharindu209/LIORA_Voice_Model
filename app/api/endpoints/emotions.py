from fastapi import APIRouter
from app.services.load_labels import load_label_encoder

router = APIRouter()

@router.get("/emotions/")
async def list_emotions():
    lb = load_label_encoder()
    return {"emotions": lb.classes_.tolist()}
