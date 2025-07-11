import customtkinter as ctk
from ui.home import load_home_ui
from ui.estilo import cargar_icono

class LoginFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(expand=True)

        icono = cargar_icono("img/instrumining.ico", size=(120, 120))
        if icono:
            ctk.CTkLabel(self, image=icono, text="").pack(pady=(20, 0))
        else:
            ctk.CTkLabel(self, text="INSTRUMINING", font=("Helvetica", 22, "bold")).pack(pady=20)

        ctk.CTkLabel(self, text="Iniciar sesión", font=("Helvetica", 16, "bold")).pack(pady=10)

        self.username = ctk.CTkEntry(self, placeholder_text="Usuario", width=220)
        self.password = ctk.CTkEntry(self, placeholder_text="Contraseña", show="*", width=220)
        self.username.pack(pady=5)
        self.password.pack(pady=5)

        ctk.CTkButton(self, text="Ingresar", command=self.autenticar).pack(pady=15)
        ctk.CTkLabel(self, text="© 2025 Instrumining SpA", font=("Arial", 8)).pack(side="bottom", pady=10)

    def autenticar(self):
        print("Autenticando a:", self.username.get())
        self.pack_forget()  # ✅ Oculta solo el login
        load_home_ui(self.master)  # ✅ Reutiliza la misma ventana