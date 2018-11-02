"""
Created on Mon Oct 29 21:44:45 2018
@author: M.C. Rogelio Manuel Higuera Gonzalez
TecnolÃ³gico Nacional de MÃ©xico
Departamento de ingenierÃ­a electrÃ³nica
CaracterÃ­stica Id vs Vd de un diodo
"""
import numpy as np
import matplotlib.pyplot as plt
datos1=np.loadtxt("datos1.txt",usecols=(0,1,),skiprows=1)#Lee datos de la simulacion de ORCAD
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
Vdex=np.linspace(-0.6,1,num=9) #Datos experimentales de voltaje del diodo
Idex=np.array([0,0,0,0,0,0.069,0.531,30.8,126.8]) #Datos experimentales de la corriente del diodo
Vdsi=(datos1[:,0]) #Datos de voltaje del diodo de la simulacion en ORCAD
Idsi=(datos1[:,1]) #Datos de corriente del diodo de la simulacion en ORCAD
fig,axes1=plt.subplots() #Crear una Figura para la grafica
axes1.plot(Vd,mA*Id) #Grafica (Vd vs Id) de los datos de la ecuacion
axes1.plot(Vdex,Idex) #Grafica (Vd vs Id) de los datos experimentales
axes1.plot(Vdsi,mA*Idsi) #Grafica (Vd vs Id) de los datos de la simulacion
axes1.set_title('CaracterÃ­stica del diodo semiconductor de silicio') #Nombre de la grafica
axes1.set_xlabel('Vd (V)') #Nombre del eje x
axes1.set_ylabel('Id (mA)') #Nombre del eje y
plt.grid(True) #Activa la cudricula
plt.savefig('IdvsVd.jpg',depi=1000) #Guarda la grafica como imagen
