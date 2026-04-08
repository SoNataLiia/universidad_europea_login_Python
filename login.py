import os
import tkinter as tk
from tkinter import ttk, messagebox
import sys
# 1.datos
USUARIOS_VALIDOS = [
    {"nombre": "admin",    "contrasena": "admin123",  "cargo": "Administrador"},
    {"nombre": "profesor", "contrasena": "prof2025",  "cargo": "Profesor"},
    {"nombre": "alumno",   "contrasena": "alumno01",  "cargo": "Alumno"},
]
CARGOS = ["Administrador", "Profesor", "Alumno"]

#2.ventana principal
ventana = tk.Tk()
ventana.title("Universidad Europea")
ventana.resizable(False, False)

frame_cabecera = tk.Frame(ventana, bg="white", pady=10)
frame_cabecera.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10)

# el logo ue.png
ruta_logo = os.path.join(os.path.dirname(__file__), "ue.png")
try:
    img_logo = tk.PhotoImage(file=ruta_logo)
    img_logo = img_logo.subsample(max(1, img_logo.width() // 80))
    lbl_logo = tk.Label(frame_cabecera, image=img_logo, bg="white")
    lbl_logo.image = img_logo  # mantener referencia
    lbl_logo.pack(side="left", padx=(0, 10))
except Exception:

    canvas_logo = tk.Canvas(frame_cabecera, width=60, height=60,
                            bg="white", highlightthickness=0)
    canvas_logo.pack(side="left", padx=(0, 10))
    canvas_logo.create_rectangle(0, 0, 60, 60, fill="#E8001C", outline="")
    canvas_logo.create_text(30, 32, text="ue",
                            font=("Georgia", 22, "bold"), fill="white")

lbl_titulo = tk.Label(frame_cabecera, text="Universidad\nEuropea",
                      font=("Arial", 16, "bold"), bg="white", justify="left")
lbl_titulo.pack(side="left")



#3.campos
# nombre
tk.Label(ventana, text="NOMBRE").grid(
    row=2, column=0, padx=10, pady=8, sticky="w")
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.grid(row=2, column=1, padx=10, pady=8, sticky="w")

# contraseña
tk.Label(ventana, text="CONTRASEÑA").grid(
    row=3, column=0, padx=10, pady=8, sticky="w")
entrada_contrasena = tk.Entry(ventana, show="*", width=30)
entrada_contrasena.grid(row=3, column=1, padx=10, pady=8, sticky="w")

# cargo
tk.Label(ventana, text="CARGO").grid(
    row=4, column=0, padx=10, pady=8, sticky="w")
combo_cargo = ttk.Combobox(ventana, values=CARGOS, state="readonly", width=27)
combo_cargo.set("Selecciona una opción")
combo_cargo.grid(row=4, column=1, padx=10, pady=8, sticky="w")

# area mensaje
area_texto = tk.Text(ventana, height=5, width=44, state="disabled")
area_texto.grid(row=5, column=0, columnspan=2, padx=10, pady=8)

# tabla
tk.Label(ventana, text="Usuarios válidos:",
         font=("Arial", 9, "bold")).grid(
    row=6, column=0, columnspan=2, padx=10, pady=(6, 2), sticky="w")

frame_tabla = tk.Frame(ventana)
frame_tabla.grid(row=7, column=0, columnspan=2, padx=10, pady=(0, 6))

tabla = ttk.Treeview(frame_tabla,
                     columns=("nombre", "contrasena", "cargo"),
                     show="headings", height=3)
tabla.heading("nombre", text="Nombre")
tabla.heading("contrasena", text="Contraseña")
tabla.heading("cargo", text="Cargo")
tabla.column("nombre", width=120, anchor="center")
tabla.column("contrasena", width=120, anchor="center")
tabla.column("cargo", width=130, anchor="center")

for u in USUARIOS_VALIDOS:
    tabla.insert("", "end", values=(u["nombre"], u["contrasena"], u["cargo"]))

tabla.pack()

#botones
frame_botones = tk.Frame(ventana)
frame_botones.grid(row=8, column=0, columnspan=2, pady=12)

tk.Button(frame_botones, text="LIMPIAR", width=12, command=lambda: limpiar()).pack(side="left", padx=5)
tk.Button(frame_botones, text="ENTRAR", width=12, command=lambda: entrar()).pack(side="left", padx=5)
tk.Button(frame_botones, text="SALIR", width=12, command=lambda: salir()).pack(side="left", padx=5)


# mensaje
def mostrar_mensaje(texto):
    area_texto.config(state="normal")
    area_texto.delete("1.0", tk.END)
    area_texto.insert("1.0", texto)
    area_texto.config(state="disabled")


# limpiar
def limpiar():
    entrada_nombre.delete(0, tk.END)
    entrada_contrasena.delete(0, tk.END)
    combo_cargo.set("Selecciona una opción")
    mostrar_mensaje("Formulario limpiado.")


# entrar
def entrar():
    nombre = entrada_nombre.get().strip()
    contrasena = entrada_contrasena.get().strip()
    cargo = combo_cargo.get()

    if not nombre or not contrasena or cargo == "Selecciona una opción":
        mostrar_mensaje("Por favor, completa todos los campos.")
        return

    valido = any(
        u["nombre"] == nombre and
        u["contrasena"] == contrasena and
        u["cargo"] == cargo
        for u in USUARIOS_VALIDOS
    )

    if valido:
        mostrar_mensaje(f"Acceso concedido. Bienvenido/a, {nombre}.\nCargo: {cargo}.")
    else:
        mostrar_mensaje("Datos incorrectos. Comprueba nombre, contraseña y cargo.")


# salir
def salir():
    if messagebox.askyesno("Salir", "¿Deseas cerrar la aplicación?"):
        ventana.destroy()
        sys.exit(0)
#iniciar

ventana.mainloop()