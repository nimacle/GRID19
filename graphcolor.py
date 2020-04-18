# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:54:55 2020

@author: matth
"""
n=int(input(""))
a=int(900/n)
b=0
c=0
liste1=["red","blue","green","black","yellow"]*(int(n/5)+1)
Matrice=[0]*n
for i in range(n):
    Matrice[i]=liste1
    
type(Matrice)
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        ''''Tout les objets (widgets) apparaissant sur la fenetre tkinter'''
        self.a = tk.Canvas(self)#canvas sur lequel est dessiné toutes les personnes (carré)
        self.a["width"] = "900"     #taille du canvas
        self.a["height"] = "900"
        self.a.pack(side="left")    #alignement 
        for b in range(n):
            for c in range(n):
                self.a.create_rectangle(b*a,c*a,(b*a)+a, (c*a)+a,fill=Matrice[b][c])    #création des personnes

        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.change)  #bouton de fermeture (qui sert actuellement a rafraichir la page)
        self.quit.pack(side="right")    #alignement de la page
        
    def change(self):
    '''actualisation de la fenetre en fonction des nouvelles valeurs'''
        for b in range(n):
            for c in range(n):
                self.a.create_rectangle(b*a,c*a,(b*a)+a, (c*a)+a,fill="white")
        app.update()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
