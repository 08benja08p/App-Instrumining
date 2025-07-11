# ui/modbus.py
import customtkinter as ctk

def build_modbus_tab(parent):
    frame = ctk.CTkFrame(parent)

    ctk.CTkLabel(frame, text="📡 Datos Modbus", font=("Helvetica", 16)).pack(pady=20)
    ctk.CTkLabel(frame, text="Aquí podrás monitorear variables y escribir registros.").pack()

    return frame