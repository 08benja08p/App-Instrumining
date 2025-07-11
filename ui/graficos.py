# ui/graficos.py
import customtkinter as ctk

def build_graficos_tab(parent):
    frame = ctk.CTkFrame(parent)

    ctk.CTkLabel(frame, text="📊 Visualización de gráficos", font=("Helvetica", 16)).pack(pady=20)
    ctk.CTkLabel(frame, text="Aquí se desplegarán gráficos en tiempo real o históricos.").pack()

    return frame
