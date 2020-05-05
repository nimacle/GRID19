# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:54:55 2020
@author: matth
"""
import tkinter as tk
import tkinter.font as tkFont
import numpy as np
import main
'''
ligne1=[0,1,0,0,0]
ligne2=[0,0,0,0,0]
ligne3=[0,0,1,0,0]
ligne4=[0,1,0,0,0]
ligne5=[0,0,0,1,0]

Matrice=np.array([ligne1,ligne2,ligne3,ligne4,ligne5])

Matrice=Matrice.astype(str)
Matrice=np.where(Matrice=="0",'black',Matrice)
Matrice=np.where(Matrice=="1",'red',Matrice)
'''


class Application(tk.Frame):
    '''fenetre de l'application graphique'''
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure()
        self.pack()
        self.j=0
        self.infecte=tk.StringVar(value="Nombre d'infecté au jour 0 : 1")
        self.sain=tk.StringVar()
        self.EP()



    def delete_frame(self):
        '''Fonction qui vide la fenetre'''
        for widget in self.winfo_children():
            widget.destroy()

    def EP(self):
        ''' Widget pour la fenetre principal'''
        #titre de la fenetre
        self.titrefenetre0 = tk.Label(self,text="Bienvenue sur ce programme de simulation d'épidémie")
        self.titrefenetre0.grid(row=0,column=0)

        #curseur pour la population
        self.populationtitle = tk.Label(self,text="Population : ")
        self.populationtitle.grid(row=2,column=0)
        self.population = tk.Scale(self, width=25,orient=tk.HORIZONTAL,length=200,from_=1,to=200)
        self.population.grid(row=2,column=1)

        #curseur de R(infectiosité)
        self.Rtitle = tk.Label(self,text="R : ")
        self.Rtitle.grid(row=3,column=0)
        self.RR = tk.Scale(self, width=25,orient=tk.HORIZONTAL,length=200,from_=0,to=4,resolution=0.1)
        self.RR.grid(row=3,column=1)

        #bouton d'acces a la page de selection du mode de visualisation de l'epidémie
        self.accesES = tk.Button(self, text="Simuler", fg="black",command=self.ES)
        self.accesES.grid(column=5,row=5)

        # Bouton pour quitter l'application
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)#bouton de fermeture (qui sert actuellement a rafraichir la page)
        self.quit.grid(column=5,row=6)    #alignement de la page

    def ES(self):
        '''widgets de la Fenetre de selection du mode de visualisation'''
        self.n=self.population.get()    #récupération dans deux variables de la population (racine de la population car cotée du carré)
        self.R=self.RR.get()
        self.sain.set("Nombre de personnes saines au jour 0 : "+str(self.n**2-1))
        self.list_j=main.Simulation(50,self.n,self.R)

        # Convertiseur de chaque matrice de la liste en matrice de couleurs
        for i in range(51):
            self.list_j[i]=self.list_j[i].astype(str)
            self.list_j[i]=np.where(self.list_j[i]=="0",'black',self.list_j[i])
            self.list_j[i]=np.where(self.list_j[i]=="1",'red',self.list_j[i])

        self.delete_frame() #Supression des widgets pour la nouvelle fenêtre


        #Titre fenetre de selection du mode de visualisation
        self.titrefenetre1= tk.Label(self,text="Menu de selection du mode de visualisation des données\n",font=tkFont.Font(size=20))
        self.titrefenetre1.grid(columnspan=3)

        #Bouton d'acces a E1, simulation de la dispertion dans la pop
        self.accesE1 = tk.Button(self, text="Visualisé l'épidémie se répendre ", fg="black",command=self.E1)
        self.accesE1.grid(column=1,row=2)

        #Bouton vers autre menu(WIP)
        self.accesE1 = tk.Button(self, text="A décidé ", fg="black")
        self.accesE1.grid(column=1,row=3)

        # Bouton pour quitter l'application
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)  #bouton de fermeture (qui sert actuellement a rafraichir la page)
        self.quit.grid(column=3,row=4)    #alignement de la page

    def E1(self):
        ''''widgets de la fenetre de visualisation de l'épidémie qui se répend'''


        self.a=int(900/self.n)  #taille d'une personne (carré)

        b=0
        c=0
        liste1=["red","blue","green","black","yellow"]*(int(self.n/5)+1)
        Matrice=[0]*self.n
        for i in range(self.n):
            Matrice[i]=liste1

        self.delete_frame()     #on vide la frame
        #canvas sur lequel est dessiné toutes les personnes (carré)
        self.canvas = tk.Canvas(self)    #création du canvas
        self.canvas["width"] = "900"     #taille du canvas
        self.canvas["height"] = "900"
        self.canvas.grid(column=0,columnspan=25,rowspan=25)    #alignement
        for b in range(self.n): #Absisse
            for c in range(self.n): #Ordonnée
                self.canvas.create_rectangle(b*self.a,c*self.a,(b*self.a)+self.a, (c*self.a)+self.a,fill=self.list_j[0][c][b])    #création des personnes

        self.label_infecté = tk.Label(self,textvariable=self.infecte)
        self.label_infecté.grid(row=8, column=26)

        self.label_sain = tk.Label(self,textvariable=self.sain)
        self.label_sain.grid(row=9, column=26)

        # Selecteur échelle qui permet de selectionner le jour
        self.scale = tk.Scale(self, width=25,orient=tk.HORIZONTAL,length=200,from_=0,to=50)
        self.scale.grid(row=11,column=26)

        # Bouton d'actualisation des couleurs
        self.change = tk.Button(self, text="Change", fg="black",command=self.change)
        self.change.grid(column=26,row=13)

        # Bouton pour quitter l'application
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)  #bouton de fermeture (qui sert actuellement a rafraichir la page)
        self.quit.grid(column=26,row=14)    #alignement de la page


    def change(self):

        '''actualisation de la fenetre en fonction des nouvelles valeurs''' #pour l'instant uniquement un choix de couleurs

        for b in range(self.n): #Absisse
            for c in range(self.n):    #Ordonnée
                if app.list_j[self.j][c][b]!=app.list_j[self.scale.get()][c][b]:
                    self.canvas.create_rectangle(b*self.a,c*self.a,(b*self.a)+self.a, (c*self.a)+self.a,fill=self.list_j[self.scale.get()][c][b])
        self.j=self.scale.get()
        self.infecte.set("Nombre d'infecté au jour "+str(self.j)+" : "+str(np.count_nonzero(self.list_j[self.j]=='red')))
        self.sain.set("Nombre de personnes saines au jour "+str(self.j)+" : "+str(np.count_nonzero(self.list_j[self.j]=='black')))

        app.update()



root = tk.Tk()
app = Application(master=root)
app.mainloop()
