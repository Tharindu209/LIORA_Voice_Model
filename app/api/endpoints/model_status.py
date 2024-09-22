from fastapi import APIRouter

router = APIRouter(
    tags=["status"],
)

@router.get("/model_status")
async def model_status():
    return {"status": "Model is loaded and ready"}
