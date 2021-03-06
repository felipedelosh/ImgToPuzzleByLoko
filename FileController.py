"""
file controller...
if ned create, read files or folders
"""
import os
from os import scandir
from random import randint


class FileController:
    def __init__(self):
        self.rutaDelProyecto = str(os.path.dirname(os.path.abspath(__file__))) # En donde estoy padado

    def loadRandomPuzzleImage(self):
        """
        get a [] to /recursos/images/#
        """
        try:
            folders = []

            for i in scandir(self.rutaDelProyecto+"//recursos//images"):
                if i.is_dir() and i.name != "null":
                    folders.append(i.name)
                    
            dir = self.rutaDelProyecto + "//recursos//images//"
            id = folders[randint(0, len(folders)-1)]

            if self.verifyPuzzleFolderIntegrity(dir, id):
                files = []
                for i in range(0, 8):
                    files.append(dir+id+"//"+str(i+1)+".gif")

                return files
            else:
                return ["recursos/images/1/1.gif", "recursos/images/1/2.gif", "recursos/images/1/3.gif", "recursos/images/1/4.gif", "recursos/images/1/5.gif", "recursos/images/1/6.gif","recursos/images/1/7.gif","recursos/images/1/8.gif"]

        except:
            return ["recursos/images/1/1.gif", "recursos/images/1/2.gif", "recursos/images/1/3.gif", "recursos/images/1/4.gif", "recursos/images/1/5.gif", "recursos/images/1/6.gif","recursos/images/1/7.gif","recursos/images/1/8.gif"]


    def verifyPuzzleFolderIntegrity(self, dir, id):
        """
        Verify
        1 -> the namefolder is int
        """
        try:
            a = int(id)

            imgOK = True

            for i in scandir(dir+id):
                imgOK = imgOK and i.is_file and ".gif" in i.name

            return a>0 and imgOK
        except:
            return False


    def loadRandomNullPointer(self):
        """
        all imagen contain  a pointer N
        """
        try:
            nombreArchivos = []
            for i in scandir(self.rutaDelProyecto+"//recursos//images//null"):
                if i.is_file():
                    if ".gif" in i.name:
                        nombreArchivos.append(i.name)

            return self.rutaDelProyecto+"//recursos//images//null//" + nombreArchivos[randint(0, len(nombreArchivos)-1)]
        except:
            return self.rutaDelProyecto+"//recursos//images//null//1.gif"

         


    def loadMessages(self):
        """
        return {} data of /recursos/database/mensajes.txt
        """
        try:
            data = {}
            f = open(self.rutaDelProyecto+"\\recursos\\database\\mensajes.txt", "r", encoding="UTF-8")

            for i in f.read().split("\n"):
                if i.strip()!="":
                    k = i.split(":")
                    data[k[0]] = k[1]

            return data
             
        except:
            return {}

    def saveMessage(self, n, msm):
        """
        Enter #, Msm
        And save in hable position to 
        """
        # load Mesajes
        data = self.loadMessages()
        data[n] = msm

        data = self.orderMessages(data)

        try:
            f = open(self.rutaDelProyecto+"\\recursos\\database\\mensajes.txt", "w", encoding="UTF-8")
            txt = ""
            for i in data:
                txt = txt + str(i) + ":" + data[i] + "\n"
            f.write(txt)
            f.close()
            
        except:
            pass



    def orderMessages(self, data):
        """
        enter {#:msm, #:msm} and order DESC
        """
        n = []
        d = []
        for i in data:
            n.append(int(i))
            d.append(data[i])

        #Bubble short
        tempN = 0
        tempD = ""

        for i in range(0, len(n)):
            for j in range(0, len(n)-1):
                if n[j] > n[j+1]:
                    tempN = n[j]
                    tempD = d[j]
                    n[j] = n[j+1]
                    d[j] = d[j+1]
                    n[j+1] = tempN
                    d[j+1] = tempD     

        orderData = {}
        
        for i in range(0, len(n)):
            orderData[n[i]] = d[i]

        return orderData


    def loadScore(self):
        """
        Return {} data of /recursos/database/topScore.txt
        """
        try:
            data = {}
            f = open(self.rutaDelProyecto+"\\recursos\\database\\topScore.txt", "r", encoding="UTF-8")

            for i in f.read().split("\n"):
                if i.strip()!="":
                    k = i.split(":")
                    data[k[0]] = k[1]

            return data
             
        except:
            return {}

    def saveScore(self, n, player):
        """
        Enter #:Player
        is record in able position to  /recursos/database/topScore.txt
        """
        # Load scores
        data = self.loadScore()
        # Insert nre player
        data[n] = player

        data = self.orderScores(data)

        try:
            f = open(self.rutaDelProyecto+"\\recursos\\database\\topScore.txt", "w", encoding="UTF-8")
            txt = ""
            for i in data:
                txt = txt + str(i) + ":" + data[i] + "\n"
            f.write(txt)
            f.close()
            
        except:
            pass




    def orderScores(self, data={}):
        """
        enter a {#:player, #:player ...} and order by DESC
        """
        n = []
        d = []
        for i in data:
            n.append(int(i))
            d.append(data[i])

        #Bubble short
        tempN = 0
        tempD = ""

        for i in range(0, len(n)):
            for j in range(0, len(n)-1):
                if n[j] > n[j+1]:
                    tempN = n[j]
                    tempD = d[j]
                    n[j] = n[j+1]
                    d[j] = d[j+1]
                    n[j+1] = tempN
                    d[j+1] = tempD     

        orderData = {}
        
        for i in range(0, len(n)):
            orderData[n[i]] = d[i]

        return orderData
