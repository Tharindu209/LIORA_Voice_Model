# Emotion Prediction Backend

This project is a FastAPI-based backend for predicting emotions from audio files. 

## Setup

1. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file with the following content:
    ```env
    MODEL_PATH=model/Emotion_Model_aug.h5
    MODEL_JSON_PATH=model/model_json_aug.json
    LABELS_PATH=labels/labels.pickle
    UPLOAD_FOLDER=app/static/upload
    ASSEMBLYAI_API_KEY=your_assemblyai_api_key_here
    ```

4. Run the application:
    ```sh
    uvicorn app.main:app --reload
    ```

## Endpoints

- `/predict` - POST - Predict emotion from an audio file
- `/health` - GET - Check the health status of the application
- `/model_status` - GET - Check the status of the loaded model
- `/emotions` - GET - Get the list of supported emotions
- `/batch_predict` - POST - Predict emotions from multiple audio files
- `/transcribe_and_predict` - POST - Transcribe and predict


also want the python 3.10

3.10.8