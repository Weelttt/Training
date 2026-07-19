import tkinter as tk

window = tk.Tk()
window.title("Weather APP")
window.geometry("500x450+150+100")
window.resizable(False, False)

title = tk.Label(window, text="Clima Actual", font=("Arial", 30))
title.grid(row=0, column=1, pady=20)

temperature = tk.Label(window, text="--- °C", font=("Arial", 25))
temperature.grid(row=1, column=1, pady=20)

city = tk.Label(window, text="Ciudad : Santiago", font=("Arial", 20))
city.grid(row=2, column=1, pady=20)

search = tk.Entry(window, text="Buscar")
search.grid(row=3, column=1, pady=20)

status = tk.Label( window,text="---",font=("Arial", 10))
status.grid(row=4, column=0, columnspan=1, pady=20)

humidity = tk.Label(window, text="---", font=("Arial", 10))
humidity.grid(row=4, column=1, columnspan=2,  pady=20)

window.mainloop()
