import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.getenv('MODEL_PATH', 'model/Emotion_Model_aug.h5')
LABELS_PATH = os.getenv('LABELS_PATH', 'labels/labels.pickle')
