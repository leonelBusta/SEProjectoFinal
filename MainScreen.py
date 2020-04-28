#importar las librerias
from tkinter import *
from tkinter import messagebox
import sqlite3

#Creacion de la ventana principal
root = Tk()


#Crear la barra del menu
barraMenu = Menu (root)


#Configurar los parametros de la ventana principal
root.config(menu = barraMenu, height = 200, width = 400)


# Contruiremos la primer opción del menú
bConexion = Menu(barraMenu, tearoff = 0)
bdConexion.add_command(label="Conexion Base de Datos (B.D)")
bConexion.add_command(label="Salir...")


#Contruiremos la segunda opción del menú
bLimpiar=Menu(barraMenu, tearoff = 0)
bLimpiar.add_command(label="Limpiar campos")


#Contruiremos la tercera opción del menú
bCrud = Menu(barraMenu, tearoff = 0)
bCrud.add_command(label="Create")
bCrud.add_command(label="Read")
bCrud.add_command(label="Update")
bCrud.add_command(label="Delete")


#Contruiremos la cuarta opción del menú
bAyuda = Menu(barraMenu, tearoff = 0)
bAyuda.add_command(label="Ayuda...")
bAyuda.add_command(label="Acerca de...")


##### Asignamos las opciones creadas al menu
barraMenu.add_cascade(label="CONEXIÓN B.D", menu=bConexion)
barraMenu.add_cascade(label="LIMPIAR", menu=bLimpiar)
barraMenu.add_cascade(label="C-R-U-D", menu=bCrud)
barraMenu.add_cascade(label="AYUDA", menu=bAyuda)


#Creamos un bucle
root.mainloop()