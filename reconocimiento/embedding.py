from deepface import DeepFace
import json
import numpy as np
import os

RUTA_EMBEDDINGS = "data/embeddings.json"


def generar_embedding(frame, modelo="Facenet", enforce_detection=False):
    embedding = DeepFace.represent(
        img_path=frame,
        model_name=modelo,
        enforce_detection=enforce_detection
    )[0]["embedding"]
    return embedding

def cargar_embeddings():
    if os.path.exists(RUTA_EMBEDDINGS):
        with open(RUTA_EMBEDDINGS, "r") as f:
            return json.load(f)
    return {}

def comparar_embeddings(embedding1, embedding2, threshold=0.6):
    return np.linalg.norm(np.array(embedding1) - np.array(embedding2)) < threshold