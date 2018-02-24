import tkinter as tk
#Imports everything from tkinter library

LARGE_FONT= ('Verdana', 12)

#main gui window
class Window(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame
        frame.grid(row=0, column=0,sticky='nsew')
        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def qf():
    print ("HELLO\n")

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text='Start Page', font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text='visit page 1', 
                            command=None)
        button1.pack()
app = Window()
app.mainloop()
