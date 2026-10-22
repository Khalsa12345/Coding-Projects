import tkinter as tk

window = tk.Tk()
window.title('First Window')
window.geometry('300x200')

label = tk.Label(window, text='First Window')
label.pack(pady=20)

label2 = tk.Label(window, text='Cold init')
label2.pack(pady=(20,30))#Pady is how much space is above and below text.
                         #if there are two numbers, it will show how much
                         #space above and below seperatly




window.mainloop()
