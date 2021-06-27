from tkinter import *
from primerImagen import PrimerImagen
from segundaImagen import SegundaImagen
from terceraImagen import TerceraImagen
from cuartaImagen import CuartaImagen
from quintaImagen import QuintaImagen

class Ventana:
    def __init__(self):

        raiz = Tk()

        #Modificación de la ventana

        raiz.title("Proyecto de Tesseract") #Modificar el titulo

        # raiz.resizable(0,0) #Este es para redimensionar la ventana

        raiz.iconbitmap("editor-de-texto.ico") #Asignar un icono a la venta

            # raiz.geometry("750x450") #Tamaño de la ventana

        raiz.config(bg="#323") #Asigar color a la ventana

        raiz.config(bd="10")

        raiz.config(relief="sunken")

        raiz.config(cursor="hand2")

            #Creación del Frame

        miFrame = Frame() #Creación del Frame

            # miFrame.pack(fill="both", expand="true") #Con esto se puede expandir

        miFrame.pack()

        miFrame.config(bg="#323") #Damos color al Frame

        miFrame.config(width="650", height="350") #Se debe dar medidas al Frame y la Raiz toma estas medidas

        miFrame.config(bd="10")

        miFrame.config(relief="sunken")

        miFrame.config(cursor="pirate")

            #Label que muestra el titulo

        miLabel = Label(miFrame, text="Proyecto de Tesseract", font=("Comic Sans MS",18))

        miLabel.place(x=160, y=20)

            #Creacion de los botones

            #Primer boton "Imagen1"
        botonImagen1 = Button(raiz, command=PrimerImagen, text="Imagen Uno") #Boton con una funcion que vuelve una imagen de otro tamaño
        botonImagen1.place(x=40,y=200)
    

            #Segundo boton "Imagen2"
        botonImagen2 = Button(raiz, command=SegundaImagen, text="Imagen Dos") 
        botonImagen2.place(x=158,y=200)
    

            #Tercer boton "Imagen3"
        botonImagen3 = Button(raiz, command=TerceraImagen, text="Imagen Tres") 
        botonImagen3.place(x=276,y=200)
      

            #Cuarto boton "Imagen4"
        botonImagen4 = Button(raiz, command=CuartaImagen, text="Imagen Cuatro") 
        botonImagen4.place(x=394,y=200)
        

            #Quinto boton "Imagen5"
        botonImagen5 = Button(raiz, command=QuintaImagen, text="Imagen Cinco") 
        botonImagen5.place(x=512,y=200)
       


        raiz.mainloop() #Este metodo siempre al final xd

Ventana()