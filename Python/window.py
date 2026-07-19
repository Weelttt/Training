import tkinter as tk

ventana = tk.Tk()

ventana.title ("Conversor de Welt")
ventana.geometry("600x400+150+100")
ventana.resizable(False,False)


text = tk.Label(ventana, text="Hola")
text.pack()

def saludar():
    text.config(text="Bienvenido👋")
    
button = tk.Button(ventana, text="Saludar", command=saludar)
button.pack()
    

ventana.mainloop()