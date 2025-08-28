import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
from reconocimiento.verificador import reconocer_empleado


class Interfaz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Control de Ingresos y Egresos")
        self.root.geometry("800x600")

        tk.Label(self.root, text="Control de Empleados", font=("Arial", 16)).pack(pady=20)

        # Botón para iniciar el registro de ingreso
        tk.Button(self.root, text="Registrar Ingreso", command=lambda: self.capturar_rostro("Ingreso")).pack(pady=10)

        # Botón para iniciar el registro de egreso
        tk.Button(self.root, text="Registrar Egreso", command=lambda: self.capturar_rostro("Egreso")).pack(pady=10)

        self.video_label = tk.Label(self.root)
        self.video_label.pack()

        self.cap = None
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def start_camera(self):
        """Inicia el bucle de la cámara para mostrar el video."""
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
        self.update_frame()

    def update_frame(self):
        """Actualiza el frame de la cámara en el QLabel y detecta caras."""
        # Se asegura de que la cámara esté activa antes de leer un frame
        if self.cap is not None and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

                # Dibujar el recuadro verde en cada cara detectada
                for (x, y, w, h) in faces:
                    cv2.rectangle(cv2image, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Convertir la imagen para mostrarla en Tkinter
                img = Image.fromarray(cv2image)
                imgtk = ImageTk.PhotoImage(image=img)
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)

            self.root.after(30, self.update_frame)  # Llama a update_frame en 30ms

    def capturar_rostro(self, tipo):
        """Detiene la cámara, captura un solo frame y lo procesa para el reconocimiento."""
        # Se asegura de que la cámara esté activa para poder leer un frame
        if self.cap is not None and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

                if len(faces) > 0:
                    x, y, w, h = faces[0]
                    face_img = frame[y:y + h, x:x + w]

                    try:
                        empleado = reconocer_empleado(face_img)
                        if empleado:
                            messagebox.showinfo("Éxito", f"¡{tipo} registrado para {empleado}!")
                        else:
                            messagebox.showerror("Error", "Empleado no reconocido.")
                    except ValueError:
                        messagebox.showerror("Error", "No se pudo procesar la cara. Intente de nuevo.")

                else:
                    messagebox.showerror("Error",
                                         "No se detectó ninguna cara. Por favor, asegúrese de que su cara esté visible en la cámara.")

            # Libera la cámara y limpia el label después de procesar
            self.cap.release()
            self.cap = None
            self.video_label.configure(image='')

    def iniciar(self):
        """Inicia la interfaz y el bucle de la cámara."""
        self.start_camera()
        self.root.mainloop()


if __name__ == "__main__":
    app = Interfaz()
    app.iniciar()

