from fastapi import APIRouter

router = APIRouter(
    tags=["Status"],
)

@router.get("/health/")
async def health_check():
    return {"status": "OK"}
