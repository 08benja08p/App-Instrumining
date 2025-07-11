# ui/home.py
import customtkinter as ctk
from ui.inicio import build_inicio_tab
from ui.camaras import build_camaras_tab
from ui.graficos import build_graficos_tab
from ui.modbus import build_modbus_tab
from ui.ajustes import build_ajustes_tab

def load_home_ui(master):
    master.title("Instrumining App")
    master.geometry("1000x700")

    notebook = ctk.CTkTabview(master)
    notebook.pack(expand=True, fill="both", padx=10, pady=10)

    # Crear pestañas sin contenido aún
    notebook.add("Inicio")
    notebook.add("Cámaras")
    notebook.add("Gráficos")
    notebook.add("Modbus")
    notebook.add("Ajustes")

    # Insertar contenido a cada pestaña
    build_inicio_tab(notebook.tab("Inicio")).pack(expand=True, fill="both")
    build_camaras_tab(notebook.tab("Cámaras")).pack(expand=True, fill="both")
    build_graficos_tab(notebook.tab("Gráficos")).pack(expand=True, fill="both")
    build_modbus_tab(notebook.tab("Modbus")).pack(expand=True, fill="both")
    build_ajustes_tab(notebook.tab("Ajustes")).pack(expand=True, fill="both")

