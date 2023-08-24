'''
Universidad del Valle de Guatemala
Parcial 1 - Física 3
Simulación de Campo Eléctricos
 ---> Cálculo de campos

Fabiola Contreras 22787
María José Villafuerte 22129
'''

# Importamos las librerías necesarias para la simulación.
import numpy as np # Libreria científica y matemática para Python.
from scipy import constants, integrate   # Librerias para integrar funciones en un intervalo dado.

'''
Diccionario: 
K: Contante de Coulomb
Q: Carga
r:Radio 
x: Distancia apunto P
l: largo de la línea de carga

'''

k = 8.988*10**9 #Valor de 1/4π∈₀
#ecuacion_general_CampoE = (k*Q)/(r**2)

'''Funcion que calcula el campo electrico en una línea de carga.'''
def Funcion_ecuacion_CampoE_LineasDeCarga(Q,x,l):
    #Ya que le pedimos la lingutod debemos de dividirlo por 2
    a = l/2
    dE = lambda y: (k*Q*x)/(l*np.sqrt(x**2+y**2)**3)
    E = integrate.quad(dE, -a, a) 
    print('El valor del campo es:',"{:.3e}".format(E[0]))

'''Funcion que calcula el campo electrico en un anillo circular.'''
def Funcion_ecuacion_CampoE_anillo(Q,x,a):
    r = np.sqrt(x**2+a**2)
    s = 2*np.pi*a
    lamda= Q/((2)(np.pi)(a))
    dE = lambda s: (k*(lamda)*x)/(l*np.sqrt(x**2+y**2)**3)
    E = integrate.quad(dE, 0, (2)(np.pi)(a)) 
    result = 0
    return result
    
'''Funcion que calcula el campo electrico en un disco circular.'''
def Funcion_ecuacion_CampoE_Disco(Q,x,R):
    result = 0
    return result