'''
Universidad del Valle de Guatemala
Parcial 1 - Física 3
Simulación de Campo Eléctricos
 ---> Menú principal

Fabiola Contreras 22787
María José Villafuerte 22129
'''

import tkinter as tk # Libreria para creacion de interfaz grafica
import calc
import graficas

def clear_frame():
    for widgets in Main_page.winfo_children():
      widgets.destroy()

def campoE_Linea():
    clear_frame()
    tk.Label(Main_page, text = "\t Línea de carga", font="Times 25").place(x=100, y=10)

    tk.Label(Main_page, text = "Ingresa el largo de la línea de carga", font="Times 8").place(x=10, y=40)
    Input_Largo_linea = tk.DoubleVar()
    tk.Entry(textvariable=Input_Largo_linea).place(x=10,y=65)

    tk.Label(Main_page, text = "Ingresa la carga del elemento", font="Times 8").place(x=10, y=80)
    Input_Carga = tk.DoubleVar()
    tk.Entry(textvariable=Input_Carga).place(x=10,y=105)

    tk.Label(Main_page, text = "Ingresa la distancia 'x' entre la partícula y la línea", font="Times 8").place(x=10, y=120)
    Input_Distancia = tk.DoubleVar()
    tk.Entry(textvariable=Input_Distancia).place(x=10,y=145)

    def Call_calculation():
        calc.Funcion_ecuacion_CampoE_LineasDeCarga(Input_Carga.get(), Input_Distancia.get(), Input_Largo_linea.get())
        #graficas.Grafica_CampoE_LineasDeCarga(x=Input_Distancia, Direccion="+")
        #PENDIENTE: mostrar resultado en interfaz

    Boton_listo = tk.Button(text ="Listo", command= Call_calculation)
    Boton_listo.place(x=15, y=170)

    
def campoE_Anillo():
    clear_frame()
    tk.Label(Main_page, text = "\t Anillo de carga", font="Times 25").place(x=100, y=10)

    tk.Label(Main_page, text = "Ingresa el radio del anillo", font="Times 8").place(x=10, y=40)
    Input_radio = tk.DoubleVar()
    tk.Entry(textvariable=Input_radio).place(x=10,y=65)

    tk.Label(Main_page, text = "Ingresa la carga del elemento", font="Times 8").place(x=10, y=80)
    Input_Carga = tk.DoubleVar()
    tk.Entry(textvariable=Input_Carga).place(x=10,y=105)

    tk.Label(Main_page, text = "Ingresa la distancia 'x' entre la partícula y el anillo", font="Times 8").place(x=10, y=120)
    Input_Distancia = tk.DoubleVar()
    tk.Entry(textvariable=Input_Distancia).place(x=10,y=145)

    def Call_calculation():
        calc.Funcion_ecuacion_CampoE_anillo(float(Input_Carga.get()), float(Input_Distancia.get()), float(Input_radio.get()))
        #graficas.Grafica_CampoE_anillo(x=Input_Distancia, Direccion="+")
        #PENDIENTE: mostrar resultado en interfaz

    Boton_listo = tk.Button(text ="Listo", command= Call_calculation)
    Boton_listo.place(x=15, y=170)

def campoE_Disco():
    clear_frame()
    tk.Label(Main_page, text = "\t Disco", font="Times 25").place(x=100, y=10)
    
    tk.Label(Main_page, text = "Ingresa el radio del disco", font="Times 8").place(x=10, y=40)
    Input_radio = tk.DoubleVar()
    tk.Entry(textvariable=Input_radio).place(x=10,y=65)

    tk.Label(Main_page, text = "Ingresa la carga del elemento", font="Times 8").place(x=10, y=80)
    Input_Carga = tk.DoubleVar()
    tk.Entry(textvariable=Input_Carga).place(x=10,y=105)

    tk.Label(Main_page, text = "Ingresa la distancia 'x' entre la partícula y el disco", font="Times 8").place(x=10, y=120)
    Input_Distancia = tk.DoubleVar()
    tk.Entry(textvariable=Input_Distancia).place(x=10,y=145)

    def Call_calculation():
        calc.Funcion_ecuacion_CampoE_Disco(float(Input_Carga.get()), float(Input_Distancia.get()), float(Input_radio.get()))
        #graficas.Grafica_CampoE_Disco(x=Input_Distancia, Direccion="+")
        #PENDIENTE: mostrar resultado en interfaz

    Boton_listo = tk.Button(text ="Listo", command= Call_calculation)
    Boton_listo.place(x=15, y=170)

Main_page = tk.Tk()
Main_page.geometry("750x550")

Label_pregunta = tk.Label(Main_page, text = "¿Qué tipo de campo eléctrico deseas calcular?", font="Times 20 italic").place(x=10,y=50)

Label_linea = tk.Label(Main_page, text = "\t Línea de carga", font="Times 15").place(x=5, y=120)
Boton_linea = tk.Button(text ="▷", command= campoE_Linea).place(x=240, y=118)

Label_anillo = tk.Label(Main_page, text = "\t Anillo", font="Times 15").place(x=5, y=150)
Boton_anillo = tk.Button(text ="▷", command = campoE_Anillo).place(x=240, y=148)

Label_disco = tk.Label(Main_page, text = "\t Disco", font="Times 15").place(x=5, y=180)
Boton_disco = tk.Button(text ="▷", command = campoE_Disco).place(x=240, y=178)

Main_page.mainloop()
