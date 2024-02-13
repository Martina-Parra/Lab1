"""Experimento 1: Bola que cae en un plano inclinado.
Primero se midio el tiempo sin ver: ¨list_t¨
Luego, se midió el tiempo, viendo : ¨list_t1 """

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

list_t = [1.150, 1.160, 1.060, 1.460, 1.800, 1.470, 1.900,1.600, 1.310, 1.860, 1.560, 1.230, 1.110, 1.150, 1.160, 1.560, 1.190, 1.530, 1.150, 1.090, 0.940, 0.790, 0.810, 0.900, 0.850, 1.540, 1.270, 1.320, 0.950, 0.740, 1.490, 1.440, 0.910, 1.300, 0.960, 1.580, 1.150, 1.00, 1.260, 0.880, 1.070, 1.520, 1.450, 1.380, 1.160, 1.560, 1.190, 1.570, 1.120, 1.640]
#list_t = np.genfromtxt("tiempos-sin-ver.txt")
list_t1= [1.090, 1.070, 1.070, 1.130, 1.170, 1.230, 1.320, 1.340, 1.240, 1.400, 1.240, 1.060, 1.370, 1.090, 1.030, 1.000, 0.910, 0.970, 0.880, 0.940, 1.000, 1.200, 1.070, 1.000, 1.140, 1.200, 1.110, 1.450, 1.210, 1.040, 1.050, 0.930, 1.070, 1.460, 1.400, 1.120, 1.190, 1.010, 1.040, 1.050, 1.160, 1.810]
num_mediciones1 = list(np.arange(1, (len(list_t1)+ 1)))
num_mediciones = list(np.arange(1, (len(list_t)+ 1)))




#Promedio y desviasión estándar para list_t
promed= np.mean(list_t)
desv = np.std(promed, ddof= 1)

#print("Promedio list_t: "+str(promed))
#print("Desviación estándar list_t1: "+str(desv))


#Promedio y desviasión estándar para list_t
promed1= np.mean(list_t1)
desv = np.std(promed, ddof= 1)

print("Promedio list_t: "+str(promed))
print("Desviación estándar list_t1: "+str(desv))



#Curva "viendo"
plt.scatter(num_mediciones1, list_t1, label = "viendo", color= "red")
plt.xlabel("n° de medición")
plt.ylabel("Tiempo [s]")
plt.hlines(promed1, 0, 52, label= "promedio viendo")
#plt.errorbar(num_mediciones1, list_t1, yerr= 0.005, label= "viendo")

#Curva "sin ver"
plt.scatter(num_mediciones, list_t, label = "sin ver", color= "black", marker=r'$\clubsuit$')
plt.hlines(promed, 0, 52, label= "promedio sin ver")
#plt.errorbar(num_mediciones, list_t, yerr= 0.005, label= "sin ver")
plt.legend(loc = 4)

np.histogram(list_t1)

plt.show()
#plt.savefig("Experimento1.png")

