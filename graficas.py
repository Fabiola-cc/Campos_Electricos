'''
Universidad del Valle de Guatemala
Parcial 1 - Física 3
Simulación de Campo Eléctricos
 ---> Graficación de campos

Fabiola Contreras 22787
María José Villafuerte 22129
'''
import tkinter as tk # Libreria para creacion de interfaz grafica
import turtle

def Grafica_CampoE_LineasDeCarga(x,Direccion):
    turtle.pu()
    turtle.setposition(-200,0)
    turtle.pd()
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(200)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(200)
    turtle.lt(90)
    turtle.pu()
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.pd()
    turtle.fd(x*20)
    turtle.done()
     # Cerrar la ventana al hacer clic
    turtle.exitonclick()

    
def Grafica_CampoE_anillo(x,Direccion): 
    turtle.penup()  # Levantar el lápiz
    turtle.goto(0, -100)  # Mover el cursor al centro
    turtle.pendown()  # Bajar el lápiz

    # Iniciar el relleno
    turtle.begin_fill()

    # Dibujar el anillo exterior
    turtle.circle(100)
    turtle.end_fill()

    # Posicionar para el anillo interior
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.pendown()

    # Dibujar el anillo interior
    turtle.color("black", "white")
    turtle.begin_fill()
    turtle.circle(90)
    turtle.end_fill()
    
    #Linea x
    turtle.penup()
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.pendown()
    turtle.fd(x*60)
    


    # Cerrar la ventana al hacer clic
    turtle.exitonclick()


def Grafica_CampoE_Disco(x,Direccion):
    asd =0 
    
#Grafica_CampoE_LineasDeCarga(4,4)
Grafica_CampoE_anillo(5,4)