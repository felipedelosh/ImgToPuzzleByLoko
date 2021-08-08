"""
Loko Puzzle v2.0

Dada un img[].gif organizar
"""

from os import path
from sys import platform
from tkinter import *
from Controller import Controller

class SOFTWARE:
    def __init__(self):
        self.controller = Controller()
        self.scream = Tk()
        self.canvas = Canvas(self.scream, height=700, width=600, bg="snow")
        self.canvas.bind_all("<Key>",self.press_key)
        self.lblCantidadPasos = Label(self.canvas, text="cantidad de Pasos: ")
        self.imagesRutes = self.getBgImages() # get a ramdon image
        self.nullImage = self.getNullImage() # get a pointer in image
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

        self.isActiveWindowInsertScore = False
        
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

        self.lblCantidadPasos.place(x=20, y=20)


        self.scream.after(0, self.repaint)
        self.scream.mainloop()


    def repaint(self):
        
        count = 0

        for i in self.controller.tablero:
            k = self.canvas.find_withtag("token"+str(count))
            self.canvas.itemconfigure(k, image=self.allPhotoImages[i-1])
            count = count + 1
        
        count = 0

        self.scream.after(30, self.repaint)


    def setAPPtitle(self, text):
        self.scream.title(text)

    def refrestCountSteps(self):
        self.lblCantidadPasos['text'] = "cantidad de Pasos: " + str(self.controller.cantidadMovimientos)

    def getBgImages(self):
        return self.controller.getRandomIMG()


    def getNullImage(self):
        return self.controller.getNullPointer()

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

        """Re-Arrange"""
        if str(event.keysym) == "space" and not self.controller.gameIsRun and not self.isActiveWindowInsertScore:
            self.controller.reStartgame()

        """Re-Start"""
        if str(event.keysym) == "r" and self.controller.gameIsRun and not self.isActiveWindowInsertScore:
            self.controller.reStartgame()

        self.refrestCountSteps()

        if self.controller.isGameOver() and not self.isActiveWindowInsertScore:
            self.ventanaInsertScore()
            self.isActiveWindowInsertScore = True


        
    def ventanaInsertScore(self):
        t = Toplevel()
        t.geometry("400x300")
        t.title("Game Over")
        t.protocol("WM_DELETE_WINDOW", lambda : self.closeTopLevelWindowScore(t))

        canvas = Canvas(t, height=300, width=400)
        lblCantidadPasos = Label(canvas, text="Felicitaciones has ganado!")
        lblCantidadPasos.place(x=20, y=20)
        lblNombre = Label(canvas, text="Ingresa tu nombre: ")
        lblNombre.place(x=20, y=50)
        txtNombre = Entry(canvas, width=40)
        txtNombre.place(x=150, y=52)
        lblCantidadPasos = Label(canvas, text="Deja tu mensaje: ")
        lblCantidadPasos.place(x=20, y=80)
        txtMensaje = Entry(canvas, width=40)
        txtMensaje.place(x=150, y=80)
        lblPuesto = Label(canvas, text="Puesto: ")
        lblPuesto.place(x=160, y=120)
        canvas.create_line(0, 150, 400, 150)
        lblNombreAnterior = Label(canvas, text="Primer Jugador!!!")
        lblNombreAnterior.place(x=20, y=170)
        lblCantidadPasosAnterior = Label(canvas, text="El primero no siempre es el mejor!!!")
        lblCantidadPasosAnterior.place(x=20, y=190)


        btnSave = Button(canvas, text="SAVE", bg="green", command= lambda : self.saveScore(txtNombre.get(), txtMensaje.get(), t))
        btnSave.place(x=180, y=250)
        canvas.place(x=0, y=0)

    def saveScore(self, name, message, t):
        """
        When the game is over
        Saving a input data of player
        """
        if name.strip() != "" and message.strip():
            self.controller.saveScore(name, message)
            
        self.isActiveWindowInsertScore = False
        t.destroy()

    def closeTopLevelWindowScore(self, t):
        t.destroy()
        self.ventanaInsertScore()

        
    

s = SOFTWARE()