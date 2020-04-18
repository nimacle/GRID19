import numpy as np
import pandas
import matplotlib.pyplot as plt


"""
with open('C:/Users/henri/Downloads/COVID-19-master/cssecovid19data/cssecovid19dailyreports/04-13-2020.csv','r') as f:

    data = f.readlines()
    list_country=[]
    list_deaths=[]

    for line in data:
        list1 = line.split(",")
        list_country.append(list1[3])
        list_deaths.append(list1[7])

    print(list_country)
"""

ligne1=[0,1,0,0,0]
ligne2=[0,0,0,0,0]
ligne3=[0,0,1,0,0]
ligne4=[0,1,0,0,0]
ligne5=[0,0,0,1,0]

print(ligne1)
print(ligne2)
print(ligne3)
print(ligne4)
print(ligne5)


Matrice=np.array([ligne1,ligne2,ligne2,ligne3,ligne4,ligne5])

print(Matrice[0][1])



for day in range(0,1000):

    #calcul des changements d'états

    #phase de coloriage






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
#M = mortalité
def change(Population, R, S, ):
