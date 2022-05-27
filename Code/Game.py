from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
import os
from playsound import playsound
from threading import Thread
import threading
import time



class Game:
    def __init__(self):
        self.__ventana=None
        self.__enemy_x=650
        self.__enemy_y=50
        self.__player_x=170
        self.__player_y=140
        self.__cv= None

    #***************Reproducir música***********************
    def __play(self,filename):
        path = os.path.join('Sounds',filename)
        playsound(path)

    #***************Cargar Imagenes***********************
    #Entrada: Nombre de la imagen
    #Restricciones: el nombre de la imagen debe ser formato str
    #Salida: Genera la imagen
    def __loadImage(self,filename):
        path = os.path.join('Images',filename)
        imagen = PhotoImage(file=path)
        return imagen

    def __bgmusic(self):
        print("Playing sound on bg")
        self.__play("song.mp3")


    #Funcion principal
    def main(self):



        window = Tk()
        window.title("GAME")
        window.minsize(800,600)
        window.resizable(width=NO, height=NO)
        window.configure(background="white")  
        self.__cv= Canvas(window, width= 2000, height = 2000, bg="white")
        
        self.__cv.place(x=0,y=0)
        bg= self.__loadImage("bg.png")
        f1= self.__loadImage("p2.png")
        ship= self.__loadImage("shiprm.png")
        #bullet= loadImage("bullet.png")
        self.__cv.create_image(425,320, image = bg)  
        self.__cv.create_image(self.__enemy_x,self.__enemy_y, image = f1, tags = "enemy")
        self.__cv.create_image(170,140, image = ship, tags = "player")
        #self.__cv.create_image(140,enemy_y, image = bullet, tags = "bullet")

         #*********************SHELL***************************



        #Move player
        def up(e):
            self.__player_y-=20
            x = 0
            y = -20
            self.__cv.move("player", x, y)
            self.__play("move.mp3")

        def down(e):
            self.__player_y+=20
            x = 0
            y = 20
            self.__cv.move("player", x, y)
            self.__play("move.mp3")

        def left(e):
            self.__player_x-=20
            x = -20
            y = 0
            self.__cv.move("player", x, y)
            play("move.mp3")

        def right(e):
            
            self.__player_x+=20
            x = 20
            y = 0
            self.__cv.move("player", x, y)
            play("move.mp3")

        window.bind("<Up>", up)
        window.bind("<Down>", down)
        window.bind("<Left>", left)
        window.bind("<Right>", right)
        window.mainloop()
    

        



x = Game()
x.main()


