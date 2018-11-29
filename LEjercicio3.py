print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------- Ejercicio 3 ----------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
#Ejercicio3
# Este codigo debe permitir hacer una estimacion bayesiana de parametros. Los datos CircuitoRC.txt tienen los datos de la carga de un condensador en un circuito RC. Su codigo debe estimar los parametros de R y C que resulten en el mejor ajuste de sus datos. 
# 1) IMPRIMA los mejores de valores de R y C encontrados
# 2) GRAFIQUE los datos originales y su ajuste. Guarde la grafica SIN MOSTRARLA en Ajuste.pdf. 

import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = np.loadtxt('CircuitoRC.txt')
x_data=data[:,0]
y_data=data[:,1]

Rguess= 11.0
Cguess= 20.0

R_walk = np.empty((0))
C_walk = np.empty((0))
l_walk = np.empty((0))

R_walk = np.append(R_walk, Rguess)
C_walk = np.append(C_walk, Cguess)

def likelihood(y_obs, y_model):
    chi_squared = 0.5*sum((y_obs-y_model)**2)/len(x_data)
    return np.exp(-chi_squared)

def modelo(t_data, R, C):
    return (10.0*C)*(1-np.exp(-t_data/(R*C)))

n_iterations = 20000

# Complete el codigo (puede reescribir lo anterior si prefiere que su codigo tenga otra estructura)
# 1) IMPRIMA los mejores de valores de R y C encontrados
# 2) GRAFIQUE los datos originales y su ajuste. Guarde la grafica SIN MOSTRARLA en Ajuste.pdf. 
plt.plot(x_data,y_data)
plt.show()
