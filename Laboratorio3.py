#Laboratorio 3 DABM
#Alan Javier Sarmiento Andrade


import os
import serial
import struct
import csv

arduino = serial.Serial('COM4', 9600)



def registros(valores):
        cwd = os.getcwd()
        ruta = cwd + "/LABORATORO 3/"
        ruta = ruta + "/valores.csv" 

        with open(ruta, "a",newline="") as file:
            writer = csv.writer(file,delimiter=";")
            writer.writerow(valores)

print('Bienvenido, el presente código tiene como finalidad variar la intensidad luminica de un led')
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Ingresar rango de valores', accion1),
        '2': ('Activar proceso', accion2)
    }

    generar_menu(opciones, '2')


def accion1():
    print()
    global max
    global min
    max1 = float(input("Digite el valor máximo que desea: "))
    min1 = float(input("Digite el valor mínimo que desea: "))
    valores = [max1, min1]
    registros(valores)
    print() 



def accion2():
    print()
    with open("csv/valores.csv", "r") as file:
        lectura = csv.reader(file, delimiter= ";")
        for fila in lectura:
            max = float(fila[0])
            min = float(fila[1])
    while (True):
        data = arduino.readline().decode().strip()
        if (data == ''):
            data = max
        sensor = float(data)
        valor = int((max - sensor) * 255 / (max - min))
        print()
        print('El valor luminico es:', data)
        
        if (valor > 255):
            valor = 255
        elif (valor < 0):
            valor = 0
        
        arduino.write(struct.pack(">B",valor))




if __name__ == '__main__':
    menu_principal()