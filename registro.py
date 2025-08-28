import tkinter as tk
from tkinter import messagebox
import datetime
import csv
from captura.camara import capturar_foto
from reconocimiento.verificador import reconocer_empleado
def registrar(self, tipo):
    foto = capturar_foto()
    if foto:
        empleado = reconocer_empleado(foto)
        if empleado:  # Si se encuentra en el JSON
            self.guardar_registro(empleado, tipo)
            messagebox.showinfo("OK", f"{tipo} registrado para {empleado}")
        else:  # No está en el JSON
            messagebox.showerror("Error", "Empleado no reconocido")