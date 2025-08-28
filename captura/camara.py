import cv2

def capturar_frame(timeout=5):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No se pudo abrir la cámara")
        return None

    frame_detectado = None
    start_time = cv2.getTickCount() / cv2.getTickFrequency()
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        if len(faces) > 0:
            frame_detectado = frame
            break

        elapsed = (cv2.getTickCount() / cv2.getTickFrequency()) - start_time
        if elapsed > timeout:
            break

    cap.release()
    cv2.destroyAllWindows()
    return frame_detectado