import numpy as np
from .embedding import cargar_embeddings, generar_embedding, comparar_embeddings


def reconocer_empleado(frame, umbral=0.8):

    base = cargar_embeddings()

    # Le paso la cara recortada y enforce_detection=False
    emb_capturado = generar_embedding(frame, enforce_detection=False)

    for nombre, emb_guardado in base.items():
        if comparar_embeddings(emb_capturado, emb_guardado, threshold=umbral):
            return nombre
    return None