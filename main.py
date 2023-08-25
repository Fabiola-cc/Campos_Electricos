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

def main():
    clear_frame()
    tk.Label(Main_page, text = "¿Qué tipo de campo eléctrico deseas calcular?", font="Times 20 italic").place(x=10,y=50)

    tk.Label(Main_page, text = "\t Línea de carga", font="Times 15").place(x=5, y=120)
    tk.Button(text ="▷", command= campoE_Linea).place(x=240, y=118)

    tk.Label(Main_page, text = "\t Anillo", font="Times 15").place(x=5, y=150)
    tk.Button(text ="▷", command = campoE_Anillo).place(x=240, y=148)

    tk.Label(Main_page, text = "\t Disco", font="Times 15").place(x=5, y=180)
    tk.Button(text ="▷", command = campoE_Disco).place(x=240, y=178)

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
        E = calc.Funcion_ecuacion_CampoE_LineasDeCarga(float(Input_Carga.get()), float(Input_Distancia.get()), float(Input_Largo_linea.get()))
        graficas.Grafica_CampoE_LineasDeCarga(float(Input_Distancia.get()), E)

    Boton_listo = tk.Button(text ="Listo", command= Call_calculation)
    Boton_listo.place(x=15, y=170)

    Boton_atras = tk.Button(text ="Regresar", command= main)
    Boton_atras.place(x=105, y=170)
    
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
        E = calc.Funcion_ecuacion_CampoE_anillo(float(Input_Carga.get()), float(Input_Distancia.get()), float(Input_radio.get()))
        graficas.Grafica_CampoE_anillo(float(Input_Distancia.get()), E)

    Boton_listo = tk.Button(text ="Listo", command= Call_calculation)
    Boton_listo.place(x=15, y=170)

    Boton_atras = tk.Button(text ="Regresar", command= main)
    Boton_atras.place(x=105, y=170)

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
        E = calc.Funcion_ecuacion_CampoE_Disco(float(Input_Carga.get()), float(Input_Distancia.get()), float(Input_radio.get()))
        graficas.Grafica_CampoE_Disco(float(Input_Distancia.get()), E)

    Boton_listo = tk.Button(text ="Listo", command= Call_calculation)
    Boton_listo.place(x=15, y=170)

    Boton_atras = tk.Button(text ="Regresar", command= main)
    Boton_atras.place(x=105, y=170)

Main_page = tk.Tk()
Main_page.geometry("750x550")
main()
Main_page.mainloop()

