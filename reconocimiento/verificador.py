from .embedding import cargar_embeddings, generar_embedding, comparar_embeddings

def reconocer_empleado(frame, umbral=0.7):
    base = cargar_embeddings()
    emb_capturado = generar_embedding(frame)

    for nombre, emb_guardado in base.items():
        if comparar_embeddings(emb_capturado, emb_guardado, threshold=umbral):
            return nombre
    return None