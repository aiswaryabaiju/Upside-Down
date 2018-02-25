import tkinter as tk
from tkinter import messagebox
#Imports everything from tkinter library

LARGE_FONT= ('Verdana', 12)

#main gui window
class Window(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'Upside-Down')

        container = tk.Frame(self)   
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menu_bar = tk.Menu(container)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Exit', command=quit)
        menu_bar.add_cascade(label= 'File', menu=file_menu)

        about_menu = tk.Menu(menu_bar, tearoff=0)
        about_menu.add_command(label='About', 
                                command=lambda:tk.messagebox.showinfo('About', 
                                'Abdul Rehman - arehman087\n' +
                                'Anatoly Tverdovsky - antverdovsky\n'+
                                'Aiswarya Baiju - aiswaryabaiju\n'+
                                'Mohammad Abdul Salam - mhdmessi'))
        
        menu_bar.add_cascade(label='Help', menu=about_menu)
        tk.Tk.config(self, menu=menu_bar)
        self.frames = {}

        for F in (StartPage, cam_page, result_page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0,sticky='nsew')
        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text='Start Page', font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text='visit page 1', 
                            command=lambda: controller.show_frame(cam_page))
        button1.pack()

class cam_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text='Camera Page', font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text='Get Result', 
                            command=lambda: controller.show_frame(result_page))
        button1.pack()

class result_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text='Result Page', font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text='Go home', 
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

app = Window()
app.mainloop()
