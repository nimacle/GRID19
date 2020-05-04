import numpy as np
import pandas
import matplotlib.pyplot as plt
import random
from math import *

#app.n=population
#app.r=transmition

def Simulation(jours, population):
    
    
    l=[0]*(jours+1)
    Matrice=np.zeros([population,population], dtype=int)

    start_x=random.randint(0,population)
    start_y=random.randint(0,population)
    Matrice[start_x][start_y]=1
    l[0]=np.copy(Matrice)
    
    for i in range(0,jours):
        result = np.where(Matrice == 1)
        listOfCoordinates= list(zip(result[0], result[1]))


        for coords in listOfCoordinates:
            x=coords[0]
            y=coords[1]

            if y==0 and x==0:                               #cas ou c'est un coin
                Matrice[x+1][y]=1
                Matrice[x][y+1]=1
                pass

            elif y==0 and x==len(Matrice)-1:
                Matrice[x-1][y]=1
                Matrice[x][y+1]
                pass

            elif y==len(Matrice)-1 and x==0:
                Matrice[x+1][y]=1
                Matrice[x][y-1]=1
                pass

            elif y==len(Matrice)-1 and x==len(Matrice)-1:
                Matrice[x-1][y]=1
                Matrice[x][y-1]=1
                pass

            else:                                           #cas ou c'est un bord non coin

                if y==0:
                    Matrice[x+1][y]=1
                    Matrice[x-1][y]=1
                    Matrice[x][y+1]=1
                    pass

                elif y==len(Matrice)-1:
                    Matrice[x-1][y]=1
                    Matrice[x+1][y]=1
                    Matrice[x][y-1]=1
                    pass

                elif x==0:
                    Matrice[x][y+1]=1
                    Matrice[x+1][y]=1
                    Matrice[x][y-1]=1
                    pass

                elif x==len(Matrice)-1:
                    Matrice[x-1][y]=1
                    Matrice[x][y+1]=1
                    Matrice[x][y-1]=1
                    pass

                else:
                    Matrice[x-1][y]=1
                    Matrice[x][y+1]=1
                    Matrice[x][y-1]=1
                    Matrice[x+1][y]=1
                    pass

        l[i+1]=np.copy(Matrice)
    return l

l=Simulation(10, 10)
