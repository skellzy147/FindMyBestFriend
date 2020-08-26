import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser
from findMyAnimals import getMyBestFriend

INTRO_TEXT = "Welcome to Find My Best Friend! \nTo find your new best friend, choose an animal below, and the program will \n find a random new best friend from ASSISI Sanctuary NI"

class Application(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.minsize(width=650, height=300)
        self.maxsize(width=650, height=300)
        self.createGUI()

    def createGUI(self):
        self.winfo_toplevel().title("Find My Best Friend!")
        self.grid()
        

        top_frame = Frame(self, bg='#f0ff6e', width = 450, height = 10)
        center = Frame(self, bg='#f0ff6e', width=50, height=100, padx=3)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        top_frame.grid(row=0, sticky=NSEW)
        top_frame.grid_rowconfigure(0, weight=1)
        top_frame.grid_columnconfigure(0, weight=1)
        center.grid(row=1, sticky=NS)
        
        bannerLabel = tk.Label(top_frame)
        bannerLabel.grid(row=0, sticky=NSEW)
        bannerLabel.configure(text=INTRO_TEXT, background="#f0ff6e")

        paddedLeft = Frame(center, bg='#f4ff96', width=50, height=190)
        buttonLayout = Frame(center, bg='#f4ff96', width=250, height=250, padx=3, pady=3)
        paddedRight = Frame(center, bg='#f4ff96', width=50, height=190, padx=3, pady=3)
        
        paddedLeft.grid(row=0, column=0, sticky=NSEW)
        buttonLayout.grid(row=0, column=1, sticky=NSEW)
        paddedRight.grid(row=0, column=2, sticky=NSEW)
        

        for x in range(5):
            buttonLayout.grid_columnconfigure(x, weight=1)
        for y in range(2):
            buttonLayout.grid_rowconfigure(y, weight=1)
                
        DOG_PHOTO = tk.PhotoImage(file="DOG.gif", master=buttonLayout).subsample(3,3)
        dog_button = ttk.Button(buttonLayout, image= DOG_PHOTO, text="Dog", command=lambda: openWebPage(getMyBestFriend("Dog")), compound= "center")
        dog_button.image = DOG_PHOTO
        dog_button.grid(row = 0, column=0, sticky=NSEW)
        
        
        CAT_PHOTO = tk.PhotoImage(file="CAT.gif", master=buttonLayout).subsample(3,3)
        cat_button = ttk.Button(buttonLayout, image = CAT_PHOTO, text="Cat", command=lambda: openWebPage(getMyBestFriend("Cat")), compound="center")
        cat_button.image = CAT_PHOTO
        cat_button.grid(row = 0, column=2, sticky=NSEW)

        RABBIT_PHOTO = tk.PhotoImage(file="RABBIT.gif", master=buttonLayout).subsample(3,3)
        rabbit_button = ttk.Button(buttonLayout, image = RABBIT_PHOTO, text="Rabbit", command=lambda: openWebPage(getMyBestFriend("Rabbit")), compound="center")
        rabbit_button.image = RABBIT_PHOTO
        rabbit_button.grid(row = 0, column = 4,  sticky=NSEW)

        GUINEAPIG_PHOTO = tk.PhotoImage(file="GUINEAPIG.gif", master=buttonLayout).subsample(3,3)
        guineapig_button = ttk.Button(buttonLayout, image= GUINEAPIG_PHOTO, text="Guinea Pig", command=lambda: openWebPage(getMyBestFriend("Guinea Pig")), compound="center")
        guineapig_button.image = GUINEAPIG_PHOTO
        guineapig_button.grid(row=1, column=1,  sticky=NSEW)

        SURPRISEME_PHOTO = tk.PhotoImage(file="SURPRISEME.gif", master=buttonLayout).subsample(3,3)
        surpriseme_button = ttk.Button(buttonLayout, image=SURPRISEME_PHOTO, text="Surprise Me!", command=lambda: openWebPage(getMyBestFriend()), compound="center")
        surpriseme_button.image = SURPRISEME_PHOTO
        surpriseme_button.grid(row=1, column=3,  sticky=NSEW)

        


def openWebPage(link):
    webbrowser.open(link,new=1)

bestFriendGUI = Application(None)
bestFriendGUI.mainloop()