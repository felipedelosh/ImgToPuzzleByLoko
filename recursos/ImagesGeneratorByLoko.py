"""
1 -> you need isntal pillow

python -m pip install pillow


This is the utilite to generate a 8 pieces of a 600x600.gif image

the original image :

original.gif >> only 600x600p

The output

Create a folder output and inside

1.gif, 2.gif ... 8.gif 

All imagenes represent a original in parts of 200x200p

"""

from tkinter import *
import os
from PIL import Image as convertidorImagen

class Software:
    def __init__(self):
        self.rutaDelProyecto = str(os.path.dirname(os.path.abspath(__file__))) # En donde estoy padado
        self.screem = Tk()
        self.canvas = Canvas(self.screem, height=300, width=300)
        self.lblMessage = Label(self.canvas, text="Load original Image...")
        self.btnConvert = Button(self.canvas, bg="yellow", text="Generate.", command= self.convertIMG)


        self.paintShowConfigure()

    def paintShowConfigure(self):
        self.screem.title("Img 8 Generator by loko")
        self.screem.geometry("300x300")

        self.canvas.place(x=0, y=0)
        self.lblMessage.place(x=50, y=50)
        self.btnConvert.place(x=120, y=120)


        self.screem.mainloop()

    def convertIMG(self):
        """
        open input.gif 
        and save 8 .gif 200x200p
        """
        try:
            imagen = convertidorImagen.open(self.rutaDelProyecto+"\\input.gif")

            if imagen.size == (600, 600):

                # Create a folder dir
                if not os.path.isdir(self.rutaDelProyecto+"\\output"): 
                    os.mkdir(self.rutaDelProyecto+"\\output")

                x_Limit = 0
                y_limit = 0
                for i in range(0, 8):
                    if x_Limit == 3:
                        y_limit = y_limit + 1
                        x_Limit = 0

                    imgArea = ((200*x_Limit), (200*y_limit), (200*(x_Limit+1)), (200*(y_limit+1)))

                    imgOUT = imagen.crop(imgArea)
                    imgOUT.save(self.rutaDelProyecto+"\\output\\"+str(i+1)+".gif")

                    x_Limit = x_Limit + 1
                    

                self.btnConvert['bg'] = 'green'
            else:
                self.btnConvert['bg'] = "black"


        except:
            self.btnConvert['bg'] = 'red'


s = Software()