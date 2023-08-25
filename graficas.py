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

def Grafica_CampoE_LineasDeCarga(x,E):
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

    
def Grafica_CampoE_anillo(x,E): #E campo eléctrico
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


def Grafica_CampoE_Disco(x,E):
    turtle.hideturtle()
    turtle.penup()  # Levantar el lápiz
    turtle.goto(-150, -100)  # Mover el cursor a un punto visible
    turtle.pendown()  # Bajar el lápiz

    # Iniciar el relleno
    turtle.begin_fill()

    # Dibujar el disco
    turtle.color("#D6A99A", "#D6CBC1")
    turtle.circle(100)
    turtle.end_fill()
    
    #Linea x
    turtle.penup()
    turtle.left(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.pendown()
    turtle.fd(x*60+50)

    #Ubicación de partícula
    turtle.color("black")
    turtle.penup()
    turtle.right(180)
    turtle.forward(50)
    turtle.pendown()
    turtle.circle(3)
    turtle.write("P", move=False, align='left', font=('Arial', 8, 'normal'))

    #Especificar valor de x
    turtle.color("#E16036")
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(x*60)
    turtle.right(90)
    turtle.fd(5)
    turtle.color("black")
    turtle.penup()
    turtle.right(90)
    turtle.forward(x*30-3)
    turtle.right(90)
    turtle.forward(5)
    turtle.pendown()
    turtle.write("x = " + str(x), move=False, align='left', font=('Arial', 7, 'normal'))

    #Especificar valor del campo eléctrico y mostrar dirección
    turtle.penup()
    turtle.left(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(x*30+3)
    #Variación según dirección
    if E < 0:
        turtle.right(180)
        turtle.fd(130)
        turtle.right(90)
        turtle.forward(20)
        turtle.write("Valor de campo eléctrico: " + str(E), move=False, align='left', font=('Arial', 7, 'normal'))
        turtle.right(180)
        turtle.fd(15)
        turtle.right(90)
        turtle.backward(130)
    else:
        turtle.fd(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.write("Valor de campo eléctrico: " + "{:.3e}".format(E), move=False, align='left', font=('Arial', 7, 'normal'))
        turtle.right(180)
        turtle.fd(15)
        turtle.left(90)
        turtle.backward(20)

    turtle.color("#E3170A")
    turtle.pendown()
    turtle.showturtle()
    turtle.fd(30)
    turtle.write("Dirección de E", font=('Arial', 8, 'bold'))
    

    
    # Cerrar la ventana al hacer clic
    turtle.exitonclick()
    
#Grafica_CampoE_LineasDeCarga(4,4)
#Grafica_CampoE_anillo(5,4)
#Grafica_CampoE_Disco(7,4)