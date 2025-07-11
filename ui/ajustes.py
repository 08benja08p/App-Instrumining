# ui/ajustes.py
import customtkinter as ctk

def build_ajustes_tab(parent):
    frame = ctk.CTkFrame(parent)

    ctk.CTkLabel(
        frame,
        text="⚙ Ajustes del sistema y configuraciones",
        font=("Helvetica", 16)
    ).pack(pady=20)

    ctk.CTkLabel(frame, text="Modo de Apariencia:").pack(pady=(10, 2))

    # Crear OptionMenu con evento vinculado
    opcion_tema = ctk.CTkOptionMenu(
        frame,
        values=["System", "Light", "Dark"],
        command=cambiar_apariencia  # ⚠️ aquí se enlaza
    )
    opcion_tema.set("Dark")  # Valor inicial
    opcion_tema.pack()

    return frame

# 🧠 función que se ejecuta al cambiar el valor del menú
def cambiar_apariencia(modo):
    ctk.set_appearance_mode(modo)

