import tkinter as tk
from random import choice

colors = ('red', 'orange', 'blue', 'magenta','green4') # list of colors
my_text = 'Happy Halloween!' # your Halloween greetings

def show_text(): # function which will run continuously
    color = choice(colors)
    l.config(text=my_text, fg=color, bg='black')
    root.after(500, show_text) # delay + next iteration
    
root = tk.Tk()
root.wm_overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(background='black')
root.bind("<Button-1>", lambda evt: root.destroy()) # Exit on Click

l = tk.Label(text='', font=("Ravie", 60))
l.pack(expand=True)

show_text()
root.mainloop()