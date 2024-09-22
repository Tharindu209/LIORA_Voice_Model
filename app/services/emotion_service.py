import librosa
import numpy as np
import tensorflow as tf
import pandas as pd
import asyncio
from io import BytesIO
from sklearn.preprocessing import LabelEncoder
from fastapi import UploadFile
from app.services.load_labels import load_label_encoder
from app.services.load_audio import load_audio
from app.services.load_labels import load_label_encoder
from app.services.load_audio import load_audio

# Load the model and label encoder
model = tf.keras.models.load_model('model/Emotion_Model_aug.h5', custom_objects={'Sequential': tf.keras.Sequential})
lb = load_label_encoder()

async def predict_emotion(file: UploadFile) -> str:
    y, sr = load_audio(file)
    mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13), axis=0)
    df = pd.DataFrame(data=mfccs).T
    df = np.expand_dims(df, axis=2)
    prediction = model.predict(df)
    final = prediction.argmax(axis=1)
    final = lb.inverse_transform(final)
    
    confidence = prediction.max()
    return final, confidence

async def batch_predict_emotions(files):
    results = []
    for file in files:
        emotion, confidence = await predict_emotion(file)
        results.append({"emotion": emotion, "confidence": confidence})
        
    converted_data = [
        {
            'emotion': emotion_array[0],  # Extract the string from the numpy array
            'confidence': confidence
        }
        for entry in results
        for emotion_array in [entry['emotion']]
        for confidence in [entry['confidence']]
        ]
    return converted_data

async def transcribe_and_predict(file: UploadFile):
    # Run transcription and emotion prediction in parallel
    transcription, (emotion, confidence) = await asyncio.gather(
        transcribe_audio(file.filename),
        predict_emotion(file.filename)
    )
    print(transcription, emotion[0], confidence)
    return transcription, emotion[0], confidence