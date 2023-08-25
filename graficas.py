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
    turtle.hideturtle()
    #Eje y
    turtle.pu()
    turtle.color("grey")
    turtle.goto(-145, 150)
    turtle.write("y", move=False, align='left', font=('Arial', 8, 'normal'))
    turtle.right(90)
    turtle.pd()
    turtle.fd(300)

    #Creación de línea de carga
    turtle.color("#D6A99A")
    turtle.pensize(2)
    turtle.pu()
    turtle.left(90)
    turtle.goto(-150, -100)  # Mover el cursor a un punto visible
    turtle.pd()
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(200)
    turtle.lt(90)
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(200)
    turtle.lt(90)

    #Eje x
    turtle.color("black")
    turtle.pu()
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.pd()
    turtle.fd(x*2+10)
    
    #Ubicación de partícula
    turtle.penup()
    turtle.right(180)
    turtle.forward(10)
    turtle.pendown()
    turtle.dot(5)
    turtle.write("P", move=False, align='left', font=('Arial', 8, 'normal'))

    #Especificar valor de x
    turtle.color("#E16036")
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(x*2)
    turtle.right(90)
    turtle.fd(5)
    turtle.color("black")
    turtle.penup()
    turtle.right(90)
    turtle.forward(x-3)
    turtle.right(90)
    turtle.forward(5)
    turtle.pendown()
    turtle.write("x = " + str(x), move=False, align='left', font=('Arial', 7, 'normal'))

    #Especificar valor del campo eléctrico 
    turtle.penup()
    turtle.left(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(x+3)
    #mostrar dirección
    turtle.fd(2)#derecha
    turtle.left(90)
    turtle.forward(20)#arriba
    turtle.write("Valor de campo eléctrico: " + "{:.3e}".format(E), move=False, align='left', font=('Arial', 8, 'bold'))
    turtle.right(180)
    turtle.fd(15)
    turtle.left(90)
    turtle.backward(2)

    turtle.color("#E3170A")
    turtle.pendown()
    turtle.turtlesize(stretch_wid=0.8, stretch_len=0.5)
    turtle.showturtle()
    turtle.fd(15)
    turtle.write("Dirección de E", font=('Arial', 8, 'bold'))

     # Cerrar la ventana al hacer clic
    turtle.exitonclick()
    
def Grafica_CampoE_anillo(x,E): #E campo eléctrico
    turtle.hideturtle()
    #Eje y
    turtle.pu()
    turtle.color("grey")
    turtle.goto(-150, 150)
    turtle.write("y", move=False, align='left', font=('Arial', 8, 'normal'))
    turtle.right(90)
    turtle.pd()
    turtle.fd(300)

    turtle.penup()  # Levantar el lápiz
    turtle.goto(-150, -100)  # Mover el cursor a un punto visible
    turtle.left(90)
    turtle.pendown()  # Bajar el lápiz

    # Dibujar anillo
    turtle.color("#D6A99A")
    turtle.pensize(15)
    turtle.circle(100)
    turtle.pensize(2)
    
    #Linea x
    turtle.color("black")
    turtle.penup()
    turtle.left(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.pendown()
    turtle.fd(x*2+10)

    #Ubicación de partícula
    turtle.color("black")
    turtle.penup()
    turtle.right(180)
    turtle.forward(10)
    turtle.pendown()
    turtle.dot(5, "black")
    turtle.write("P", move=False, align='left', font=('Arial', 8, 'normal'))

    #Especificar valor de x
    turtle.color("#E16036")
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(x*2)
    turtle.right(90)
    turtle.fd(5)
    turtle.color("black")
    turtle.penup()
    turtle.right(90)
    turtle.forward(x-3)
    turtle.right(90)
    turtle.forward(5)
    turtle.pendown()
    turtle.write("x = " + str(x), move=False, align='left', font=('Arial', 7, 'normal'))

    #Especificar valor del campo eléctrico
    turtle.penup()
    turtle.left(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(x+3)
    #mostrar dirección
    turtle.fd(2)
    turtle.left(90)
    turtle.forward(20)
    turtle.write("Valor de campo eléctrico: " + "{:.3e}".format(E), move=False, align='left', font=('Arial', 8, 'bold'))
    turtle.right(180)
    turtle.fd(15)
    turtle.left(90)
    turtle.backward(2)

    turtle.color("#E3170A")
    turtle.pendown()
    turtle.turtlesize(stretch_wid=0.8, stretch_len=0.5)
    turtle.showturtle()
    turtle.fd(15)
    turtle.write("Dirección de E", font=('Arial', 8, 'bold'))

    # Cerrar la ventana al hacer clic
    turtle.exitonclick()

def Grafica_CampoE_Disco(x,E):
    turtle.hideturtle()

    #Eje y
    turtle.pu()
    turtle.color("grey")
    turtle.goto(-150, 150)
    turtle.write("y", move=False, align='left', font=('Arial', 8, 'normal'))
    turtle.right(90)
    turtle.pd()
    turtle.fd(300)

    turtle.penup()  # Levantar el lápiz
    turtle.goto(-150, -100)  # Mover el cursor a un punto visible
    turtle.left(90)
    turtle.pendown()  # Bajar el lápiz

    turtle.pensize(2)
    # Dibujar el disco
    turtle.begin_fill()
    turtle.color("#D6A99A", "#D6CBC1")
    turtle.circle(100)
    turtle.end_fill()
    
    #Linea x
    turtle.penup()
    turtle.left(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.pendown()
    turtle.fd(x*2+10)

    #Ubicación de partícula
    turtle.color("black")
    turtle.penup()
    turtle.right(180)
    turtle.forward(10)
    turtle.pendown()
    turtle.dot(5, "black")
    turtle.write("P", move=False, align='left', font=('Arial', 8, 'normal'))

    #Especificar valor de x
    turtle.color("#E16036")
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(x*2)
    turtle.right(90)
    turtle.fd(5)
    turtle.color("black")
    turtle.penup()
    turtle.right(90)
    turtle.forward(x-3)
    turtle.right(90)
    turtle.forward(5)
    turtle.pendown()
    turtle.write("x = " + str(x), move=False, align='left', font=('Arial', 7, 'normal'))

    #Especificar valor del campo eléctrico y mostrar dirección
    turtle.penup()
    turtle.left(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(x+3)
    #Variación según dirección
    
    turtle.fd(2)
    turtle.left(90)
    turtle.forward(20)
    turtle.write("Valor de campo eléctrico: " + "{:.3e}".format(E), move=False, align='left', font=('Arial', 8, 'bold'))
    turtle.right(180)
    turtle.fd(15)
    turtle.left(90)
    turtle.backward(2)

    turtle.color("#E3170A")
    turtle.pendown()
    turtle.turtlesize(stretch_wid=0.8, stretch_len=0.5)
    turtle.showturtle()
    turtle.fd(15)
    turtle.write("Dirección de E", font=('Arial', 8, 'bold'))
    

    
    # Cerrar la ventana al hacer clic
    turtle.exitonclick()