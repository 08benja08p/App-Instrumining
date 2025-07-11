import customtkinter as ctk
from ui.estilo import aplicar_estilo
from ui.login import LoginFrame

if __name__ == "__main__":
    aplicar_estilo()

    app = ctk.CTk()
    app.title("Instrumining - Inicio de Sesión")
    app.geometry("420x520")
    app.iconbitmap("img/instrumining.ico")

    # Muestra login en el contexto de 'app'
    LoginFrame(master=app)
    app.mainloop()