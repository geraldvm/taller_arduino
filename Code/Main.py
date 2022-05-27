from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
from Game import Game

class Main:
    def __init__(self):
        self.__ventana=None

    #------------------------------------------
    #***************Cargar Imagenes***********************
    #Entrada: Nombre de la imagen
    #Restricciones: el nombre de la imagen debe ser formato str
    #Salida: Genera la imagen
    def __cargarImagen(self,nombre):
        if isinstance(nombre, str):
            #path = os.path.join('Imagenes',nombre)
            imagen = PhotoImage(file=nombre)
            return imagen
    #-----------------------------------------------------------
    #********************NEW GAME***************************************

    def __start(self):
        self.__newG.destroy()
        z=Game("COM6",9600)
        z.main
 

    #*****************Ventana HELP**********************
    def __help(self):

        self.__ventana.withdraw()
        self.__helpWindow = Toplevel()
        self.__helpWindow.title("Help")
        self.__helpWindow.minsize(800,600)
        self.__helpWindow.resizable(width=NO,height=NO)
        self.__cH = Canvas(self.__helpWindow, width= 800, height = 600, bg ="#096654")
        self.__cH.place(x=0,y=0)
        imh= self.__cargarImagen("images/help.png")
        self.__cH.create_image(220,180, image = imh)
        he= self.__cargarImagen("images/help_icon.png")
        self.__cH.create_image(400,180, image = he)
        #*******************Ir a ventana HOME*********************

        def home():
            self.__helpWindow.destroy()
            self.__ventana.deiconify()##Reaparece la ventana principal

        botonHome = Button(self.__helpWindow, text="Home", command=home,bg="#BF1134",fg="white",font=("Helvetica",15))
        botonHome.place(x=15,y=15)
        #***************************************************
        #Informacion de ayuda en el box texto tipo scrolled
        instructions= scrolledtext.ScrolledText(self.__cH,height=10,width=80,bg="#096654",fg="white")
        instructions.insert(END,"Presione New Game para comenzar un juego nuevo.\n" )
        instructions.insert(END,"Seguidamente ingrese los nombres de jugadores y presione la tecla OK\n" )
        instructions.insert(END,"\t\t************Gerald Valverde Mc kenzie************\n")
        
        instructions.configure(state=DISABLED)
        
                            
        instructions.place(x=100,y=400)

        self.__helpWindow.mainloop()

        
        
    #-----------------------------------------------------------------------------------        
        
        
    def __newGame(self):
        self.__ventana.withdraw()
        self.__newG = Toplevel()
        self.__newG.title("Entradas en tKinter")
        self.__newG.minsize(400,400)
        self.__newG.resizable(width=NO, height=NO)
        self.__newG.configure(background="white")  
        canvas= Canvas(self.__newG, width= 2000, height = 2000, bg="#1e2066")##ffefb2#fcedb3
        canvas.place(x=0,y=0)
        
        boton = Button(canvas,text="OK", command=self.__start,bg="#14820a",fg="white",font=("Helvetica",15)).place(x=175,y=310)
        def home():
            self.__newG.destroy()
            self.__ventana.deiconify()##Reaparece la ventana principal

        botonHome = Button(canvas, text="Home", command=home,bg="#BF1134",fg="white",font=("Helvetica",15))
        botonHome.place(x=15,y=15)
        self.__newG.mainloop()
    
    #-------------------------------------------------------------------------------
    def principal(self):
        self.__ventana = Tk()
        self.__ventana.title("GAME")
        self.__ventana.minsize(800,600)
        self.__ventana.resizable(width=NO, height=NO)
        self.__ventana.configure(background="#660920")                
        self.__fondo= Canvas(self.__ventana, width= 2000, height = 2000, bg="#751717")##ffefb2#fcedb3
        self.__fondo.place(x=0,y=0)                
        
        f1= self.__cargarImagen("images/principal.png")
                   
        self.__fondo.create_image(170,140, image = f1, tags = "f1")
        etiqueta = Label(self.__ventana,text="Board Game",font=("Comic Sans Ms",27),bg="#3a3a3a",fg="white").place(x=470,y=20)# 3f3f3f
        botonNewGame = Button(self.__ventana, text="New Game", command=self.__newGame,bg="#1e2066",fg="white",font=("Helvetica",15))
        botonNewGame.place(x=100,y=500)
        botonHelp = Button(self.__ventana, text="Help", command=self.__help,bg="#096654",fg="white",font=("Helvetica",15))
        botonHelp.place(x=510,y=500)

        self.__ventana.mainloop()
x=Main()
x.principal()