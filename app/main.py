from fastapi import FastAPI
from app.api.endpoints import predict, health, model_status, emotions, batch_predict

app = FastAPI(
    tags=["Emotion Detection API"],
)

app.include_router(predict.router)
app.include_router(health.router)
app.include_router(model_status.router)
app.include_router(emotions.router)
app.include_router(batch_predict.router)

