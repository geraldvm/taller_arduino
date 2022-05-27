from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
import os
from playsound import playsound
from threading import Thread
import threading
import time
from DriverSerial import DriverSerial


class Game:
    def __init__(self,COM,baudrate):
        self.__ventana=None
        self.__enemy_x=650
        self.__enemy_y=50
        self.__player_x=170
        self.__player_y=140
        self.__serial= DriverSerial(COM,baudrate)  
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

        def readSerial():
            while(True):
                command= self.__serial.read()
                self.__compareSerial(command)

        def sendSerial():
            command= self.__serial.send('hola'.encode())

        def th_receiveData():
            th_time=Thread(target=readSerial, args=())
            th_time.start()

        def th_sendData():
            th_time=Thread(target=sendSerial, args=())
            th_time.start()

        def closeSerial():
            self.__serial.close()

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

        #botonSTART = Button(window, text="START", command=hilo, bg="#096654",fg="white",font=("Helvetica",15)).place(x=400,y=20)
        botonArduino = Button(window, text="Arduino", command=th_receiveData, bg="#096654",fg="white",font=("Helvetica",15)).place(x=400,y=20)
        botonLED = Button(window, text="LED", command=th_sendData, bg="#096654",fg="white",font=("Helvetica",15)).place(x=200,y=20)
        botonCloseUSB = Button(window, text="Close USB", command=closeSerial, bg="#096654",fg="white",font=("Helvetica",15)).place(x=600,y=20)
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
    
    def __compareSerial(self, command):
        if(command!=None):
            if(command =='b\r\n'):
                print("BLUE")
                self.__player_y-=20
                x = 0
                y = -20
                self.__cv.move("player", x, y)
                #self.__play("move.mp3")
            elif(command=="r\r\n"):
                print("RED")
                self.__player_y+=20
                x = 0
                y = 20
                self.__cv.move("player", x, y)
                #self.__play("move.mp3")
            elif(command=="g\r\n"):
                print("GREEN")
                self.__player_x-=20
                x = -20
                y = 0
                self.__cv.move("player", x, y)
                #play("move.mp3")
            elif(command=="w\r\n"):
                #print("White")
                self.__player_x+=20
                x = 20
                y = 0
                self.__cv.move("player", x, y)
                #play("move.mp3")
            else:
                print(command)

        



x = Game("COM6",9600)
x.main()


