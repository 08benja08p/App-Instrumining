import customtkinter as ctk

def build_inicio_tab(parent):
    frame = ctk.CTkFrame(parent)
    ctk.CTkLabel(frame, text="👋 Bienvenido a la plataforma Instrumining", font=("Helvetica", 18)).pack(pady=30)
    ctk.CTkLabel(frame, text="Accede a las cámaras, datos Modbus y configuraciones desde las pestañas de arriba.").pack()
    return frame