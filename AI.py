"""
AI for puzzle By felipedelosh0

dado un vector [a,b,c,d,e,f,g,h,i] donde sus valores pueden ser 1,2,3,4,5,6,7,8,9

el vector representa>

abc
def
ghi

Se pretende ordenar basado en reglas>

1 -> El 9 representa una pieza que se puede mover arriba, abajo, 
derecha izq dependiendo si puede moverse en la matriz que representa.

"""

class Node(object):
    def __init__(self, data, childrens, euristic) -> None:
        """
        The first node by 0 the song of 0 by 1 and the new son by 3...
        """
        self.euristic = euristic # This is a numberOrder to resolve a púzzle 
        self.data = data # contain information
        self.childrens = childrens # []

class Three:
    def __init__(self) -> None:
        """
        data = puzzle status example [321875649]
        the childrens if you can mouve
        never save 2 equals childern
        childers = [<MovRight><MovDown><MovLeft><MovUP>]
        """
        self.controlList = [] # I never save 2 equal children 
        self.idControl = 0 # Unique id for every node
        self.pivot  = None # Main node 

    def addData(self, father, data):
        if self.pivot == None:
            self.pivot = Node(data, [], self.idControl)
            self.controlList.append(data)
            self.idControl = self.idControl + 1
        else:
            if data not in self.controlList:
                self._addData(self.pivot, father, data)

    def _addData(self, pivot, father, data):
        if father == pivot.data:
            pivot.childrens.append(Node(data, [], self.idControl))
            self.controlList.append(data)
            self.idControl = self.idControl + 1
        else:
            for i in pivot.childrens:
                self._addData(i, father, data)

    def searchForEuristicID(self, id):
        """
        Return a node with id
        """
        return self._searchForEuristicID(self.pivot, id)


    def _searchForEuristicID(self, node, id):
        if node.euristic == id:
            return node
        else:
            for i in node.childrens:
                result = self._searchForEuristicID(i, id)
                if result is not None: 
                    return result
            return None


    def showThree(self):
        """
        Show all data nodes
        """
        self._showThree(self.pivot)

    def _showThree(self, pivot):
        if pivot != None:
            print("Data>",pivot.data, "Eur>",pivot.euristic, "Childs: ", len(pivot.childrens))
            for i in pivot.childrens:
                self._showThree(i)

class PuzzleLokoResolver:
    def __init__(self) -> None:
        self.initialConfiguration = [] # Init a,b,c,d,e,f,h,i
        self.answer = [1,2,3,4,5,6,7,8,9] # The goal
        self.three = Three()

    def resolve(self, matrix):
        """
        1 -> create a init
        2 -> Search answer
        """
        self.initialConfiguration = matrix
        self.three.addData(None, self.initialConfiguration)
        self._searchAnswer(0)


    def _searchAnswer(self, searchEuristic):
        # Cacth Element
        print("Buscando... ID:", searchEuristic)
        nodeInfo = None
        nodeInfo = self.three.searchForEuristicID(searchEuristic)

        if nodeInfo != None:
            print("Puedo Buscar")
            if nodeInfo.data == self.answer:
                print("Encontre la respuesta...")
            else:
                print("Seguir buscando...")
                tempFatherNode = [] # Cacth father data

                for i in nodeInfo.data:
                    tempFatherNode.append(i)

                # Generate all posible childrens
                # Need search 9 to can mouve
                ninePosition = 0
                for i in tempFatherNode:
                    if i == 9:
                        break
                    ninePosition = ninePosition + 1

                # Generate a copy to save a child
                swapingNumber = 0 # to swap to 9

                # Can mouve to R
                if ninePosition != 0 and ninePosition != 3 and ninePosition != 6:
                    #print("R")
                    # Copy a table to new son
                    newChild = []
                    for i in tempFatherNode:
                        newChild.append(i)

                    swapingNumber = newChild[ninePosition - 1]
                    newChild[ninePosition - 1] = 9
                    newChild[ninePosition] = swapingNumber

                    #print(tempFatherNode, ">>" ,newChild)
                    # Save
                    self.three.addData(tempFatherNode, newChild)

                # Can mouve to down
                if ninePosition > 2:
                    #print("Down")
                    # Copy a table to new son
                    newChild = []
                    for i in tempFatherNode:
                        newChild.append(i)

                
                    swapingNumber = newChild[ninePosition - 3]
                    newChild[ninePosition - 3] = 9
                    newChild[ninePosition] = swapingNumber
                    #print(tempFatherNode, ">>" ,newChild)
                    # Save
                    self.three.addData(tempFatherNode, newChild)

                # Can mouve to L
                if ninePosition != 2 and ninePosition != 5 and ninePosition != 8:
                    #print("L")
                    # Copy a table to new son
                    newChild = []
                    for i in tempFatherNode:
                        newChild.append(i)

                    swapingNumber = newChild[ninePosition + 1]
                    newChild[ninePosition + 1] = 9
                    newChild[ninePosition] = swapingNumber
                    #print(tempFatherNode, ">>" ,newChild)
                    # Save
                    self.three.addData(tempFatherNode, newChild)

                # Can mouve to UP
                if ninePosition < 6:
                    #print("UP")
                    # Copy a table to new son
                    newChild = []
                    for i in tempFatherNode:
                        newChild.append(i)

                    swapingNumber = newChild[ninePosition + 3]
                    newChild[ninePosition + 3] = 9
                    newChild[ninePosition] = swapingNumber
                    #print(tempFatherNode, ">>" ,newChild)
                    # Save
                    self.three.addData(tempFatherNode, newChild)


                self._searchAnswer(searchEuristic+1)
        


initial = [3,2,1,8,7,5,6,4,9]

temp = [3,8,6,7,9,5,2,4,1]

oneShoot = [1,2,3,4,5,6,7,9,8]

r = PuzzleLokoResolver()
r.resolve(oneShoot)
