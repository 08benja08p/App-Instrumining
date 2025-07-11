import customtkinter as ctk
from PIL import Image

# Configuración general
def aplicar_estilo():
    ctk.set_appearance_mode("Dark")  # Light | Dark | System
    ctk.set_default_color_theme("blue")  # blue | green | dark-blue | custom json

# Cargar íconos centralmente (opcional)
def cargar_icono(ruta, size=(120, 120)):
    try:
        img = Image.open(ruta).resize(size)
        return ctk.CTkImage(light_image=img, dark_image=img, size=size)
    except Exception as e:
        print(f"⚠️ Error cargando ícono {ruta}: {e}")
        return None