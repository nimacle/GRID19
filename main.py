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

ligne1=[0,0,0,0,0]
ligne2=[0,0,1,0,0]
ligne3=[0,0,1,0,0]
ligne4=[0,1,0,0,0]
ligne5=[0,0,0,0,0]



Matrice=np.array([ligne1,ligne2,ligne3,ligne4,ligne5])


#app.n=population
#app.r=transmition
print("Matrice de départ:\n",Matrice,"\n\n")

Ligne_liste_pointeurs_malades=[]
Rang_liste_pointeurs_malades=[]

# Get the index of elements with value 15
result = np.where(Matrice == 1)

listOfCoordinates= list(zip(result[0], result[1]))


for coords in listOfCoordinates:
    x=coords[0]
    y=coords[1]

    try:
        Matrice[x-1][y]=1
        Matrice[x][y+1]=1
        Matrice[x][y-1]=1
        Matrice[x+1][y]=1

    except IndexError:      #cas ou c'est un bord
            if y==0:
                Matrice[x+1][y]=1
                Matrice[x-1][y]=1
                Matrice[x][y+1]=1

            elif y==len(Matrice):
                Matrice[x-1][y]=1
                Matrice[x+1][y]=1
                Matrice[x][y-1]=1

            else:
                pass
print(Matrice)




#for day in range(0,1):

#calcul des changements d'états
#ligne=0
#for list in Matrice:
#    rang=0
#    for value in list:          #cas ou ce n'est pas un bord
#        try:
#            if value==1:
#                #Matrice[ligne-1][rang]=1
#                #Matrice[ligne+1][rang]=1
#                #Matrice[ligne][rang-1]=1
#                Matrice[ligne][rang+1]=1
#                pass()
#
#            else:
#                pass
#
#        except IndexError:      #cas ou c'est un bord
#            if rang==0:
#                #Matrice[ligne+1][rang]=1
#                #Matrice[ligne][rang]=1
#                Matrice[ligne][rang+1]=1
#
#            elif rang==len(Matrice):
#                #Matrice[ligne-1][rang]=1
#                Matrice[ligne][rang-1]=1
#                #Matrice[ligne][rang+1]=1
#
#            else:
#                pass
#
#        rang+=1
#
#    ligne+=1
##phase de coloriage
#
#print(Matrice)
#print(len(Matrice))


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
