import tkinter as tk

ventana = tk.Tk()
ventana.title("Hola mundo")
ventana.geometry("500x150")
ventana.configure(bg="black")

etiqueta = tk.Label(
    ventana,
    text="Hola mundo, este es mi primer codigo en el curso!",
    font=("Arial", 14),
    bg="black",
    fg="white",
)
etiqueta.pack(expand=True)

ventana.mainloop()
