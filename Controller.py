"""
Controller of puzzle by loko v 2.0
"""


from random import sample
from FileController import *


class Controller:
    def __init__(self):
        # cargar/guardar archivos
        self.fileController = FileController()
        # Aqui se organizaran de manera aleatoria los numeros 1-9
        self.temp = []
        # Esto es lo que se quiere lograr
        self.estadoFinal = [1,2,3,4,5,6,7,8,9]
        # Aqui estan contenidos la casi matrix donde se pintan los numeros
        self.tablero = [1,2,3,4,5,6,7,9,8]
        self.gameIsRun = True
        # Guarda la cantidad de movimientos que ha hecho el usuario
        self.cantidadMovimientos = 0
        self.generateRandonTable()

    def saveScore(self, nombre, mensaje):
        self.fileController.saveScore(self.cantidadMovimientos, nombre)
        self.fileController.saveMessage(self.cantidadMovimientos, mensaje)

    def resetCantidadMovimientos(self):
        self.cantidadMovimientos = 0

    def isGameOver(self):
        if self.tablero == self.estadoFinal:
            self.gameIsRun = False
        return self.tablero == self.estadoFinal

    def reStartgame(self):
        self.resetCantidadMovimientos()
        self.generateRandonTable()
        self.gameIsRun = True


    def generateRandonTable(self):
        """
        ramdonmizer self.tablero
        """
        temp = []
        temp = sample(self.estadoFinal, k=len(self.estadoFinal))
        if temp == self.estadoFinal:
            self.generateRandonTable()
        else:
            self.tablero = temp

    # metodo que verifica si se puede mover.
    # Solo se encarga de buscar en que posicion esta el cero
    # luego de ello que no este en ciertas posiciones
    # mov es de tipo str 00 : up ; 01 : ri ; 10 : down ; 11 : left
    def canMouve(self, mov):
        """
        inside a command 00: up 10:Down 01:Right 11:Left
        generate a rules if you wish move up the nine ...
        [X][X][X]
        [9][9][9]
        [9][9][9]
        """
        # search a 9 piece
        donde = 0
        if self.gameIsRun:
            for i in self.tablero:
                if i == 9:
                    break
                donde = donde + 1

            if mov == "00":
                return donde < 6

            if mov == "01":
                return donde != 0 and donde != 3 and donde != 6

            if mov == "10":
                return donde > 2

            if mov == "11":
                return donde != 2 and donde != 5 and donde != 8

    def mouvePiece(self, mov):
        """
        if user press btn... and is to hable to mouve
        the nine change a position

        if mov = 00

        [2][1][3] >> [2][9][3]
        [8][9][5] >> [8][1][2]
        [6][4][7] >> [6][4][7]

        """
        
        if not self.isGameOver():
            donde = 0
            for i in self.tablero:
                if i == 9:
                    break
                donde = donde + 1

            # Declaro el candidato a intercambiar con el 9
            candidato = None

            # Para mover arriba solo hay que sumar 3
            # Capturar la pieza de abajo e intercambiar
            if mov == "00":
                candidato = self.tablero[donde + 3]
                self.tablero[donde + 3] = 9

            # Para mover derecha solo hay que restar 1
            if mov == "01":
                candidato = self.tablero[donde - 1]
                self.tablero[donde - 1] = 9

            # Para mover abajo solo hay que restar 3
            if mov == "10":
                candidato = self.tablero[donde - 3]
                self.tablero[donde - 3] = 9

            # Para mover a la izq solo se suma 1
            if mov == "11":
                candidato = self.tablero[donde + 1]
                self.tablero[donde + 1] = 9
            
            # Intercambio el 9 con la pieza contraria
            self.tablero[donde] = candidato
            self.cantidadMovimientos = self.cantidadMovimientos + 1