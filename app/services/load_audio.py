from fastapi import UploadFile
import librosa
import io

def load_audio(file: UploadFile):
    content = file.file.read()
    y, sr = librosa.load(io.BytesIO(content), sr=44100, duration=2.5)
    return y, sr