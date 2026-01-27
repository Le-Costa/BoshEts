# = ao valor minimo = -9
#abaixo da media =-1
#= a media = 0
#acima da media =1
#= ao valor maximo =9
#valores iguais recebem o valor maior 


import numpy as np 
n = 4

m = np.random.randint(0,100,(n,n))
print(m)

matriz=m.copy()
Media = int(m.mean())

print("Media:",Media)


matriz[m<Media]=-1
matriz[m==Media]=0
matriz[m>Media]=1
matriz[m==m.max()]=9
matriz[m== m.min()]=-9




print(matriz)








