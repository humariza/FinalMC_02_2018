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
Lguess=1
R_walk = np.empty((0))
C_walk = np.empty((0))
l_walk = np.empty((0))

R_walk = np.append(R_walk, Rguess)
C_walk = np.append(C_walk, Cguess)
l_walk = np.append(C_walk, Lguess)

def X2(y_obs, y_model):
    chi_squared = 0.5*sum((y_obs-y_model)**2)/len(x_data)
    return np.exp(-chi_squared)

def modelo(t_data, R, C):
    return (10.0*C)*(1-np.exp(-t_data/(R*C)))

n_iterations = 20000

for i in range(n_iterations):
	R=np.random.normal(R_walk[i],0.1)
	C=np.random.normal(C_walk[i],0.1)
	
	alfa=X2(y_data,modelo(x_data,R,C))/X2(y_data,modelo(x_data,R_walk[i],C_walk[i]))
        if(alfa>=1):
        	np.append(C_walk,C)
        	np.append(R_walk,R)
		
	 
	else:
            beta=np.random.random()
            if(alfa>=beta):
                np.append(C_walk,C)
                np.append(R_walk,R)
		
            else:
                np.append(C_walk,C_walk[i])
            	np.append( R_walk,R_walk[i]) 

##Lo de arriba esta mal pero en esencia es:
print C_walk, 'C'
print R_walk, 'R'
	

# Complete el codigo (puede reescribir lo anterior si prefiere que su codigo tenga otra estructura)
# 1) IMPRIMA los mejores de valores de R y C encontrados
# 2) GRAFIQUE los datos originales y su ajuste. Guarde la grafica SIN MOSTRARLA en Ajuste.pdf. 
plt.figure()
plt.plot(x_data,y_data,label='originales')
plt.plot(R,C)
plt.savefig('Ajuste.pdf')













