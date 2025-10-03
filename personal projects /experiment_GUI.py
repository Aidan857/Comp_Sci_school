import tkinter as tk

window = tk.Tk()
window.geometry("500x500")

window.title("My first GUI")

label = tk.Label(window, text="Hello world", font= ('Times New Roman',18))

label.pack(padx = 20, pady = 20)

textbox = tk.Text(window, height = 3, font= ('Arial',16))
textbox.pack(padx =10, pady = 10)
button = tk.Button(window, text = "cklick me !",font =('Arial',18))
button.pack(padx= 10, pady = 10)

window.mainloop()

