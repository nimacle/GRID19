import numpy as np
import pandas
import matplotlib.pyplot as plt
import random
from math import *

#app.n=population
#app.r=transmition

def Simulation(jours, population, infectiosite, mortalite):
    r=int(infectiosite*100)

    l=[0]*(jours+1)
    Matrice=np.zeros([population,population], dtype=int)
    max_r=8*100
    start_x=random.randint(0,population-1)
    start_y=random.randint(0,population-1)
    Matrice[start_x][start_y]=1
    l[0]=np.copy(Matrice)

    for i in range(0,jours):

        result = np.where(Matrice != 0)
        listOfCoordinates= list(zip(result[0], result[1]))


        for coords in listOfCoordinates:
            x=coords[0]
            y=coords[1]


            if Matrice[x][y]<8*mortalite:
                if y==0 and x==0:                               #cas ou c'est un coin
                    if random.randrange(0,max_r)<=r:
                        Matrice[x+1][y]+=1
                    if random.randrange(0,max_r)<=r:
                        Matrice[x][y+1]+=1
                    if random.randrange(0,max_r)<=r:
                        Matrice[x+1][y+1]+=1
                    continue

                elif y==0 and x==len(Matrice)-1:
                    if random.randrange(0,max_r)<=r:
                        Matrice[x-1][y]+=1
                    if random.randrange(0,max_r)<=r:
                        Matrice[x][y+1]+=1
                    if random.randrange(0,max_r)<=r:
                        Matrice[x-1][y+1]+=1
                    continue

                elif y==len(Matrice)-1 and x==0:
                    if random.randrange(0,max_r)<=r:
                        Matrice[x+1][y]+=1
                    if random.randrange(0,max_r)<=r:
                        Matrice[x][y-1]+=1
                    if random.randrange(0,max_r)<=r:
                        Matrice[x+1][y-1]+=1
                    continue

                elif y==len(Matrice)-1 and x==len(Matrice)-1:
                    if random.randrange(0,max_r)<=r:
                        Matrice[x-1][y]+=1
                    if random.randrange(0,max_r)<=r:
                        Matrice[x][y-1]+=1
                    if random.randrange(0,max_r)<=r:
                        Matrice[x-1][y-1]+=1
                    continue

                else:                                           #cas ou c'est un bord non coin

                    if y==0:
                        if random.randrange(0,max_r)<=r:
                            Matrice[x+1][y]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x-1][y]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x][y+1]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x+1][y+1]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x-1][y+1]+=1
                        continue

                    elif y==len(Matrice)-1:
                        if random.randrange(0,max_r)<=r:
                            Matrice[x-1][y]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x+1][y]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x][y-1]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x+1][y-1]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x-1][y-1]+=1
                        continue

                    elif x==0:
                        if random.randrange(0,max_r)<=r:
                            Matrice[x][y+1]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x+1][y]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x][y-1]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x+1][y+1]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x+1][y-1]+=1
                        continue

                    elif x==len(Matrice)-1:
                        if random.randrange(0,max_r)<=r:
                            Matrice[x-1][y]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x][y+1]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x][y-1]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x-1][y+1]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x-1][y-1]+=1
                        continue

                    else:
                        if random.randrange(0,max_r)<=r:
                            Matrice[x-1][y]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x][y+1]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x][y-1]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x+1][y]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x+1][y+1]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x-1][y+1]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x+1][y-1]+=1
                        if random.randrange(0,max_r)<=r:
                            Matrice[x-1][y-1]+=1
                        continue
            else:
                Matrice[x][y]=8*mortalite
        l[i+1]=np.copy(Matrice)
    return l

print(Simulation(10, 15, 8, 5))
#l[jour][ordonnée][absisses]

