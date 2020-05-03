import numpy as np
import pandas
import matplotlib.pyplot as plt
import random
from math import *


n=int(sqrt(int(input("Chosissez le nombre de population, doit etre un carré parfait (ex: 4, 9, 16, 25, 36, 49, 64, 81, 100...): "))))

Matrix=np.zeros([n,n], dtype=int)

#app.n=population
#app.r=transmition

def Simulation(Matrice, jours, population):

    start_x=random.randint(0,population)
    start_y=random.randint(0,population)
    Matrice[start_x][start_y]=1

    print("Matrice de départ:\n",Matrice,"\n\n")

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

        print(Matrice)

Simulation(Matrix,10, n)




"""
def coloriage():
    for line in Matrice:
        for value in line:
            if Matrice[x][y]==0:
                colorier en rouge
            if Matrice[x][y]==1:
"""
#Population = nombre de personnes
#R = nbre de personnes inféctées en moyenne
#S = nbre de personnes soignées/immunisées
#
#def change(Population, R, S, ):
