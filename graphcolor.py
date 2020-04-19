# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:54:55 2020
@author: matth
"""
import tkinter as tk
import tkinter.font as tkFont
import numpy as np

ligne1=[0,1,0,0,0]
ligne2=[0,0,0,0,0]
ligne3=[0,0,1,0,0]
ligne4=[0,1,0,0,0]
ligne5=[0,0,0,1,0]

Matrice=np.array([ligne1,ligne2,ligne3,ligne4,ligne5])

Matrice=Matrice.astype(str)
Matrice=np.where(Matrice=="0",'black',Matrice)
Matrice=np.where(Matrice=="1",'red',Matrice)

class Application(tk.Frame):
    '''fenetre de l'application graphique'''
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
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
        self.RR = tk.Scale(self, width=25,orient=tk.HORIZONTAL,length=200,from_=0,to=12,resolution=0.1)
        self.RR.grid(row=3,column=1)
        
        #bouton d'acces a la page de selection du mode de visualisation de l'epidémie
        self.accesES = tk.Button(self, text="Simuler", fg="black",command=self.ES)
        self.accesES.grid(column=5,row=5)
        
        # Bouton pour quitter l'application
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)  #bouton de fermeture (qui sert actuellement a rafraichir la page)
        self.quit.grid(column=5,row=6)    #alignement de la page
    
    def ES(self):
        '''widgets de la Fenetre de selection du mode de visualisation'''
        self.n=self.population.get()
        self.R=self.RR.get()
        self.delete_frame()
        
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
        '''
        b=0
        c=0
        liste1=["red","blue","green","black","yellow"]*(int(self.n/5)+1)
        Matrice=[0]*self.n
        for i in range(self.n):
            Matrice[i]=liste1
        '''
        self.delete_frame()     #on vide la frame
        #canvas sur lequel est dessiné toutes les personnes (carré)
        self.canvas = tk.Canvas(self)    #création du canvas
        self.canvas["width"] = "900"     #taille du canvas
        self.canvas["height"] = "900"
        self.canvas.grid(column=0,columnspan=25,rowspan=25)    #alignement 
        for b in range(self.n):
            for c in range(self.n):
                self.canvas.create_rectangle(b*self.a,c*self.a,(b*self.a)+self.a, (c*self.a)+self.a,fill=Matrice[b][c])    #création des personnes


        # Selecteur échelle qui permet de selectionner le jour
        self.scale = tk.Scale(self, width=25,orient=tk.HORIZONTAL,length=200,from_=100000,to=999999)
        self.scale.grid(row=11,column=26)
        
        # Bouton d'actualisation des couleurs
        self.change = tk.Button(self, text="Change", fg="black",command=self.change)
        self.change.grid(column=26,row=13)
        
        # Bouton pour quitter l'application
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)  #bouton de fermeture (qui sert actuellement a rafraichir la page)
        self.quit.grid(column=26,row=14)    #alignement de la page
        
        
    def change(self):
        '''actualisation de la fenetre en fonction des nouvelles valeurs''' #pour l'instant uniquement un choix de couleurs
        for b in range(self.n):
            for c in range(self.n):
                self.canvas.create_rectangle(b*self.a,c*self.a,(b*self.a)+self.a, (c*self.a)+self.a,fill="#"+str(self.scale.get()))
        app.update()
        
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()

