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

        button1 = tk.Button(self, text='Take a Picture!', 
                            command=lambda: controller.show_frame(cam_page))
        button1.pack()

class cam_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text='Camera Page', font = LARGE_FONT)
        label.pack(pady=10, padx=10)
        #implement portion that takes camerafeed and displays it to the user
        cam_button = tk.Button(self, text='Get Take Picture', 
                            command=lambda: None) #takes the picture by throwing keyinterrupt
        cam_button.pack(side='left')
        
        res_button = tk.Button(self, text='Get Results!', 
                            command=lambda: controller.show_frame(result_page))
        res_button.pack(side='right')

        recam_button = tk.Button(self, text='Retake Picture', 
                            command=lambda: controller.show_frame(cam_page))
        recam_button.pack(side='left')

class result_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text='Result Page', font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        scrollbar_v = tk.Scrollbar(self)
        scrollbar_v.pack(side='right', fill='y')
        links = tk.Listbox(self,yscrollcommand=scrollbar_v.set)
        
        #insert data into Listboxes

        links.pack( fill='x')

        scrollbar_v.config(command=links.yview)

        button1 = tk.Button(self, text='Go home', 
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side='bottom')

app = Window()
app.mainloop()
