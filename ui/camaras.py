# ui/camaras.py
import customtkinter as ctk

def build_camaras_tab(parent):
    frame = ctk.CTkFrame(parent)
    
    ctk.CTkLabel(frame, text="🎥 Panel de cámaras", font=("Helvetica", 16)).pack(pady=20)
    ctk.CTkLabel(frame, text="Aquí irán los streams o capturas de cámaras.").pack()

    return frame
