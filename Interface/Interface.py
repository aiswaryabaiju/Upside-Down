from tkinter import*
#Imports everything from tkinter library
from PIL import Image, ImageTk


class Window(Frame):

    def __init__(self, master = NONE):
        Frame.__init__(self, master)

#Initialization
        self.master = master
        self.init_window()
#Declaring and gonna make the function below

    def init_window(self):                                                   #Initializing the window
        self.master.title ("GUI")                                            #Title of our window = GUI
        self.pack(fill = BOTH, expand = 1)                                   #adjusts demensions as needed and fills up the window                   #


        takePic = Button(self, text ="Take Picture" )    #Text that will be written on the button
        takePic.place(x=125,y=125)

        menu = Menu(self.master)        #Menu reference to tkinter
        self.master.config(menu=menu)   #Instance of the menu

        file = Menu(menu)               #Declaring file
        file.add_command(label = 'About', command = self.showTxt)

        file.add_command(label= 'Exit', command = self.client_exit) #Adds the Exit option under file tab
        menu.add_cascade(label ='File', menu = file)                #Adds the file option in the menu


        edit = Menu(menu)                                           #Adds another tab in the option menu
        edit.add_command(label= 'Show Image', command = self.showImg)   #Adds the Undo option under edit tab
        menu.add_cascade(label = 'Edit', menu = edit)               #Adds the Undo option in the menu




    def showImg(self):
        load = Image.open('Pic.png')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image = render)
        img.image = render
        img.place (x=0,y=0)

    def showTxt(self):
        text = Label(self, text = 'Authors: mhdmessi, arehman087, antverdovsky, aiswaryabaiju')
        text.pack()
    def save(self):
        exit()
    def client_exit(self):
        exit()
    def edit_undo(self):
        exit()


root = Tk()
root.geometry("400x300")            #GUI window dimension
app = Window(root)

root.mainloop()