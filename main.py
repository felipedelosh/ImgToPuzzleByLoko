"""
Loko Puzzle v2.0

Dada un img[].gif
"""
from tkinter import *
from typing import SupportsIndex
from Controller import Controller

class SOFTWARE:
    def __init__(self):
        self.scream = Tk()
        self.canvas = Canvas(self.scream, height=700, width=600, bg="snow")
        self.canvas.bind_all("<Key>",self.press_key)
        self.imagesRutes = self.getBgImages() # get a ramdon image
        self.nullImage = self.getNullImage() # get a pointer in image
        self.controller = Controller()
        self.img1 = PhotoImage(file=self.imagesRutes[0]) 
        self.img2 = PhotoImage(file=self.imagesRutes[1]) 
        self.img3 = PhotoImage(file=self.imagesRutes[2]) 
        self.img4 = PhotoImage(file=self.imagesRutes[3]) 
        self.img5 = PhotoImage(file=self.imagesRutes[4]) 
        self.img6 = PhotoImage(file=self.imagesRutes[5]) 
        self.img7 = PhotoImage(file=self.imagesRutes[6]) 
        self.img8 = PhotoImage(file=self.imagesRutes[7])# pointer
        self.img9 = PhotoImage(file=self.nullImage)
        self.allPhotoImages = [self.img1,self.img2,self.img3,self.img4,self.img5,self.img6,self.img7,self.img8,self.img9]  
        # Images
        
        self.viewNConfigure()

    def viewNConfigure(self):
        """
        Paint a initial state
        """
        self.setAPPtitle("Puzzle by loko v2.0")
        self.scream.geometry("600x700")

        self.canvas.place(x=0, y=0)
        
        
        # Need to pain a separator lines
        for i in range(0, 2):
            self.canvas.create_line(200*(i+1)+10, 100, 200*(i+1)+10, 700, width=20)
            self.canvas.create_line(0, 200*(i+1)+100, 600, 200*(i+1)+100, width=20)

        self.canvas.create_image(0, 100, image=self.img1, anchor="nw", tags="token0")
        self.canvas.create_image(200, 100, image=self.img2, anchor="nw", tags="token1")
        self.canvas.create_image(400, 100, image=self.img3, anchor="nw", tags="token2")

        self.canvas.create_image(0, 300, image=self.img4, anchor="nw", tags="token3")
        self.canvas.create_image(200, 300, image=self.img5, anchor="nw", tags="token4")
        self.canvas.create_image(400, 300, image=self.img6, anchor="nw", tags="token5")

        self.canvas.create_image(0, 500, image=self.img7, anchor="nw", tags="token6")
        self.canvas.create_image(200, 500, image=self.img8, anchor="nw", tags="token7")
        self.canvas.create_image(400, 500, image=self.img9, anchor="nw", tags="token8")


        self.scream.after(0, self.repaint)
        self.scream.mainloop()


    def repaint(self):
        
        count = 0

        for i in self.controller.tablero:
            
            k = self.canvas.find_withtag("token"+str(count))
            self.canvas.itemconfigure(k, image=self.allPhotoImages[i-1])
            count = count + 1
        
        count = 0

        self.scream.after(100, self.repaint)
        


    def setAPPtitle(self, text):
        self.scream.title(text)

    def getBgImages(self):
        return ["recursos/images/1/1.gif", "recursos/images/1/2.gif", "recursos/images/1/3.gif", "recursos/images/1/4.gif", "recursos/images/1/5.gif", "recursos/images/1/6.gif","recursos/images/1/7.gif","recursos/images/1/8.gif"]


    def getNullImage(self):
        return "recursos/images/null/1.gif"

    def repaintImages(self):
        for i in range(0, 9):
            print(i)


    def press_key(self, event):
        """
        When you press a keyboard...
        """
        """Mov UP"""
        if str(event.keysym) == "Up":
            if self.controller.canMouve("00"):
                self.controller.mouvePiece("00")
        """Mov DOWN"""
        if str(event.keysym) == "Down":
            if self.controller.canMouve("10"):
                self.controller.mouvePiece("10")
        """Mov RI"""
        if str(event.keysym) == "Right":
            if self.controller.canMouve("01"):
                self.controller.mouvePiece("01")
        """Mov LEFT"""
        if str(event.keysym) == "Left":
            if self.controller.canMouve("11"):
                self.controller.mouvePiece("11")
    

s = SOFTWARE()