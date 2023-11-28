#...................
#IMPORTATION TKINTER
#...................

from tkinter import *

calcul = ""

#Pour afficher les calculs
def ajout_calcul(symbol):
    global calcul
    calcul +=str(symbol)
    text_resultat.delete(1.0,"end")
    text_resultat.insert(1.0,calcul)
    

#..........
# FONCTIONS
#..........

# Pour que calculer
def eval_calcul():
    global calcul
    #Pour que le programme affiche une erreur s'il y a des opérations qui contiennent des erreurs
    try:
        calcul=str(eval(calcul))
        text_resultat.delete(1.0,END)
        text_resultat.insert(1.0,calcul)
        calcul=""
    except:
        effacer_ecran()        
        text_resultat.insert(0,"Erreur")
        
        
# Pour effacer ce qu'il y a sur l'écran
def effacer_ecran(): 
    global calcul
    calcul = ""
    text_resultat.delete("1.0",END)
    

#........
# FENETRE 
#........

# Création de la première fenêtre
root=Tk() 
# Titre de l'application
root.title ("Calculatrice") 

# Style de la fenêtre
root.geometry("410x350") 
text_resultat=Text(root, height=2, width=20, font=("Arial", 24))
text_resultat.grid(columnspan=6, padx=20, pady=10)

#........
# BOUTONS
#........


# def __init__(self, valeur, font, width): 
#     self.bouton = Button(root,text=valeur, command=lambda: self.bouton_click(valeur), width=5, font=("Arial",18))
#     self.bouton.grid (font = font, width=width, padx=6, pady=6)

# def bouton_click(self, valeur):
#     current = text_resultat.get()
#     text_resultat.delete(0, "end")
#     text_resultat.insert("end", current + valeur)




#...Boutons des chiffres

btn_1=Button(root,text="1", command=lambda:ajout_calcul(1), width=5,font=("Arial",18),)
btn_1.grid(row=2, column=1)

btn_2=Button(root,text="2", command=lambda: ajout_calcul(2), width=5,font=("Arial",18))
btn_2.grid(row=2, column=2)

btn_3=Button(root,text="3", command=lambda: ajout_calcul(3), width=5,font=("Arial",18))
btn_3.grid(row=2, column=3)

btn_4=Button(root,text="4", command=lambda: ajout_calcul(4), width=5,font=("Arial",18))
btn_4.grid(row=3, column=1)

btn_5=Button(root,text="5", command=lambda: ajout_calcul(5), width=5,font=("Arial",18))
btn_5.grid(row=3, column=2)

btn_6=Button(root,text="6", command=lambda: ajout_calcul(6), width=5,font=("Arial",18))
btn_6.grid(row=3, column=3)

btn_7=Button(root,text="7", command=lambda: ajout_calcul(7), width=5,font=("Arial",18))
btn_7.grid(row=4, column=1)

btn_8=Button(root,text="8", command=lambda: ajout_calcul(8), width=5,font=("Arial",18))
btn_8.grid(row=4, column=2)

btn_9=Button(root,text="9", command=lambda: ajout_calcul(9), width=5,font=("Arial",18))
btn_9.grid(row=4, column=3)

btn_0=Button(root,text="0", command=lambda: ajout_calcul(0), width=5,font=("Arial",18))
btn_0.grid(row=5, column=2)


#...Boutons pour les parenthèses

btn_open=Button(root,text="(", command=lambda: ajout_calcul("("), width=5,font=("Arial",18))
btn_open.grid(row=5, column=1)

btn_close=Button(root,text=")", command=lambda: ajout_calcul(")"), width=5,font=("Arial",18))
btn_close.grid(row=5, column=3)


#...Boutons pour les opérations

btn_somme=Button(root,text="+", command=lambda: ajout_calcul("+"), width=5,font=("Arial",18))
btn_somme.grid(row=2, column=5)

btn_soustraction=Button(root,text="-", command=lambda: ajout_calcul("-"), width=5,font=("Arial",18))
btn_soustraction.grid(row=3, column=5)

btn_multiplication=Button(root,text="x", command=lambda: ajout_calcul("*"), width=5,font=("Arial",18))
btn_multiplication.grid(row=4, column=5)

btn_division=Button(root,text="/", command=lambda: ajout_calcul("/"), width=5,font=("Arial",18))
btn_division.grid(row=5, column=5)

btn_pourcentage=Button(root,text="%", command=lambda: ajout_calcul("%"), width=5,font=("Arial",18))
btn_pourcentage.grid(row=6, column=3)

#...Boutons effacer, égale et point 

btn_egal=Button(root,text="=", command=lambda: eval_calcul("="), width=5,font=("Arial",18))
btn_egal.grid(row=6, column=5)

btn_effacer=Button(root,text="C", command=effacer_ecran, width=5,font=("Arial",18))
btn_effacer.grid(row=6, column=1)

btn_dot=Button(root,text=".", command=lambda: ajout_calcul("."), width=5,font=("Arial",18))
btn_dot.grid(row=6, column=2)

root.mainloop()




