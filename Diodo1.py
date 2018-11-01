Diodo.py
"""
Created on Mon Oct 29 21:44:45 2018
@author: M.C. Rogelio Manuel Higuera Gonzalez
Tecnológico Nacional de México
Departamento de ingeniería electrónica
Característica Id vs Vd de un diodo
"""
import numpy as np
import matplotlib.pyplot as plt
mA=1e3 #Constante para cambiar la escala en mA
Is=1e-10 #Corriente de fuga
T=27 #Temperatura en C
Tk=273+T #Temperatura en K
q=1.6e-19 #Carga
k=1.38e-23 #Constante de Boltzmann
n=2 #Coeficiente de idealidad
VT=k*Tk/q #Voltaje termico
Vd=np.linspace(-0.5,1,num=1000) #Barrido del voltaje del diodo
Id=Is*np.exp(Vd/(n*VT)) #Corriente del diodo
fig,axes1=plt.subplots() #Crear una Figura para la grafica
axes1.plot(Vd,mA*Id) #Grafica Id vs Vd
axes1.set_title('Característica del diodo semiconductor de silicio') #Nombre de la grafica
axes1.set_xlabel('Vd (V)') #Nombre del eje x
axes1.set_ylabel('Id (mA)') #Nombre del eje y
plt.grid(True) #Activa la cudricula
plt.savefig('IdvsVd.jpg',depi=500) #Guarda la grafica como imagen
