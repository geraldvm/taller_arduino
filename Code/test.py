import serial

class DriverSerial:

    def __init__(self, port, baudrate):
        #self.__serial = serial.Serial('COM7',9600)#EDITAR COM
        self.__serial=serial.Serial(port,baudrate)
    
    def open(self):
        self.__serial.open()
    
    def close(self):
        self.__serial.close()
    
    def readbytes(self):
        if(self.__serial.inWaiting()>0):
            command=self.__serial.readline()
            return command
    
    def read(self):
        encoding= 'utf-8'
        if(self.__serial.inWaiting()>0):
            command=self.__serial.readline()
            command=command.decode(enconding)
            return command

    def send(self,data):
        self.__serial.write(data)
