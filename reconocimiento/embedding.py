import face_recognition
import json
import numpy as np
import os

RUTA_EMBEDDINGS = "data/embeddings.json"

def generar_embedding(face_img):
    # face_img es el recorte de la cara (numpy array en RGB)
    encodings = face_recognition.face_encodings(face_img)
    if encodings:
        return encodings[0].tolist()
    else:
        raise ValueError("No se pudo generar embedding para la cara recortada")

def cargar_embeddings():
    if os.path.exists(RUTA_EMBEDDINGS):
        with open(RUTA_EMBEDDINGS, "r") as f:
            return json.load(f)
    return {}

def comparar_embeddings(embedding1, embedding2, threshold=0.6):
    v1 = np.array(embedding1)
    v2 = np.array(embedding2)
    return np.linalg.norm(v1 - v2) < threshold