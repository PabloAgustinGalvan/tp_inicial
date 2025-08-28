import cv2
import json
import numpy as np
import os
from deepface import DeepFace

# Define la ruta del archivo de imagen y del archivo de embeddings
RUTA_IMAGEN = "aaa.jpg"  # <--- CAMBIA ESTA RUTA
RUTA_EMBEDDINGS = "data/embeddings.json"


def generar_embedding_desde_foto():
    """Genera el embedding de una cara a partir de una imagen y lo guarda."""

    # 1. Carga la imagen desde el disco duro
    if not os.path.exists(RUTA_IMAGEN):
        print(f"Error: La imagen no se encontró en la ruta: {RUTA_IMAGEN}")
        return

    try:
        # Genera el embedding de la cara en la imagen
        embedding = DeepFace.represent(
            img_path=RUTA_IMAGEN,
            model_name="Facenet",
            enforce_detection=True
        )[0]["embedding"]

        # 2. Pide al usuario que ingrese el nombre del empleado
        nombre = input("¡Cara detectada! Ingresa tu nombre para guardar el embedding: ")
        if not nombre:
            print("Nombre no válido. El embedding no se guardará.")
            return

        # 3. Carga los embeddings existentes o crea un diccionario vacío
        if os.path.exists(RUTA_EMBEDDINGS):
            with open(RUTA_EMBEDDINGS, "r") as f:
                data = json.load(f)
        else:
            data = {}

        # 4. Guarda el nuevo embedding en el diccionario
        data[nombre] = embedding

        # 5. Escribe el diccionario actualizado en el archivo JSON
        with open(RUTA_EMBEDDINGS, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Embedding de '{nombre}' guardado exitosamente en '{RUTA_EMBEDDINGS}'.")

    except ValueError:
        print("No se detectó una cara en la imagen. Asegúrate de que la foto cumpla con los requisitos.")
        print("Consejo: La foto debe estar bien iluminada y tener la cara de frente.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    if not os.path.exists("data"):
        os.makedirs("data")

    generar_embedding_desde_foto()