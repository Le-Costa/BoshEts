import numpy as np

n = 3
matriz = np.random.randint(0,10,(n,n))
m= matriz.reshape((3,3))
print("Matriz:\n",m)
nova = np.empty_like(m)
maior=True
for i in range(n):
    for j in range(n):
        if i != 0: 
            if m[i,j]<m[i-1,j]:#compara linha de baixo
                maior = False
        if j!=0:
            if m[i,j]<m[i,j-1]:#compara coluna de tras
                maior= False
        if i!=n-1:
            if m[i,j]<m[i+1,j]: #compara linha de baixo
                maior= False
        if j != n-1:
            if m[i,j]< m[i,j+1]: # compar coluna de cima
                maior =False
        else: 
            nova[i,j]==1











        
            
#if i !=0 and i!=n-1:# verifica se as linhas estao na extremidade
 #          if  j!=0 and j!=n-1:# verifica se as colunas estão nas extremidades
  #              if m[i,j]> m[i-1,j] and m[i,j]>m[i+1,j] and m[i,j]>m[i,j+1] and m[i,j-1]:
   #                 el= True
    #       if j==0:
               