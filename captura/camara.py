import cv2
from deepface import DeepFace

def capturar_frame(timeout=5):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("No se pudo abrir la cámara")
        return None

    frame_detectado = None
    start_time = cv2.getTickCount() / cv2.getTickFrequency()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            # Intento detectar un rostro
            DeepFace.detectFace(frame, enforce_detection=True)
            frame_detectado = frame
            break
        except Exception:
            pass  # no hay rostro, sigo

        elapsed = (cv2.getTickCount() / cv2.getTickFrequency()) - start_time
        if elapsed > timeout:
            break

    cap.release()
    cv2.destroyAllWindows()
    return frame_detectado