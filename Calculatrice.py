# Importer Tkinter ----------------------------
from tkinter import * # Tkinter

# Classes ---------------------------------------

class calculator():

    # Construction
    def __init__(saisie):
        saisie.etape1 = 0 
        saisie.etape2 = 0
        saisie.final = 0 
        saisie.entry = StringVar()
        saisie.text = "" 
        saisie.signe = "" 
        saisie.entry.set("")
        
    # Initialiser
    def init(saisie):
        saisie.etape1 = 0
        saisie.etape2 = 0
        saisie.final = 0 
        saisie.text = ""
        saisie.signe = ""
    
    # Afficher les nombres sur l'écran
    def afficher_nombre(saisie): 
        saisie.entry.set(saisie.text)
       
# Vérification du type d'opération

    def operation(saisie): 
        try : 
            if "+" in saisie.text:
                saisie.addition()
            elif "-" in saisie.text:
                saisie.soustraction()
            elif "/" in saisie.text:
                saisie.division()
            elif "x" in saisie.text:
                saisie.multiplication()            
        except:
            saisie.entry.set("Erreur")
            saisie.init()

# Addition
    def addition(saisie):
        nombre = saisie.text.split("+")
        saisie.etape1 = float(nombre[0])
        saisie.etape2 = float(nombre[1])
        saisie.final = saisie.etape1 + saisie.etape2
        saisie.entry.set(str(saisie.final))
        saisie.init()

# Soustraction
    def soustraction(saisie): 
        nombre = saisie.text.split("-")
        saisie.etape1 = float(nombre[0])
        saisie.etape2 = float(nombre[1])
        saisie.final = saisie.etape1 - saisie.etape2
        saisie.entry.set(str(saisie.final))
        saisie.init()

# Multiplication
    def multiplication(saisie):
        nombre = saisie.text.split("x")
        saisie.etape1 = float(nombre[0])
        saisie.etape2 = float(nombre[1])
        saisie.final = saisie.etape1 * saisie.etape2
        saisie.entry.set(str(saisie.final))
        saisie.init()

# Division
    def division(saisie): 
        nombre = saisie.text.split("/")
        saisie.etape1 = float(nombre[0])
        saisie.etape2 = float(nombre[1])
        saisie.final = saisie.etape1 / saisie.etape2
        saisie.entry.set(str(saisie.final))
        saisie.init()  

# Fonctions ----------------------------

# Actionnerle les boutons de 1 à 9

def Btn1 (): 
    calculatrice.text += "1"
    calculatrice.entry.set(calculatrice.text)
    
def Btn2 ():
    calculatrice.text += "2"
    calculatrice.entry.set(calculatrice.text)
    
def Btn3 ():
    calculatrice.text += "3"
    calculatrice.entry.set(calculatrice.text)
    
def Btn4 ():
    calculatrice.text += "4"
    calculatrice.entry.set(calculatrice.text)
    
def Btn5 ():
    calculatrice.text += "5"
    calculatrice.entry.set(calculatrice.text)

def Btn6 ():
    calculatrice.text += "6"
    calculatrice.entry.set(calculatrice.text)

def Btn7 ():
    calculatrice.text += "7"
    calculatrice.entry.set(calculatrice.text)

def Btn8 ():
    calculatrice.text += "8"
    calculatrice.entry.set(calculatrice.text)
    
def Btn9 ():
    calculatrice.text += "9"
    calculatrice.entry.set(calculatrice.text)
    
def Btn0 ():
    calculatrice.text += "0"
    calculatrice.entry.set(calculatrice.text)

# Actionner les boutons d'opérations

def Btn_addition ():
    calculatrice.text += "+"
    calculatrice.entry.set(calculatrice.text)

def Btn_point():
    calculatrice.text += "."
    calculatrice.entry.set(calculatrice.text)
    
def Btn_soustraction ():
    calculatrice.text += "-"
    calculatrice.entry.set(calculatrice.text)

def Btn_division ():
    calculatrice.text += "/"
    calculatrice.entry.set(calculatrice.text)

def Btn_multiplication ():
    calculatrice.text += "x"
    calculatrice.entry.set(calculatrice.text)

def Btn_operation ():
    calculatrice.operation()    

def Btn_supprimer ():
    calculatrice.entry.set("")
    calculatrice.init()
    
# Fenêtre principale ---------------------

root = Tk() 
root.geometry("430x300")
root.title("Calculatrice")

# Programme -------------------------------
calculatrice = calculator()

# Fenêtre de calcul ---------------------

fenetre=Entry(root, width=60, textvariable=calculatrice.entry, bd=6)
fenetre.grid(columnspan=6, padx=20, pady=10)

# Bouttons ----------------------------------------

# Boutons des chiffres

btn_1 = Button(root,text="1", command=Btn1, width=5,font=("Arial",18),)
btn_1.grid(row=2, column=1) 

btn_2 = Button(root,text="2", command=Btn2, width=5,font=("Arial",18))
btn_2.grid(row=2, column=2)

btn_3 = Button(root,text="3", command=Btn3, width=5,font=("Arial",18))
btn_3.grid(row=2, column=3)

btn_4 = Button(root,text="4", command=Btn4, width=5,font=("Arial",18))
btn_4.grid(row=3, column=1)

btn_5 = Button(root,text="5", command=Btn5, width=5,font=("Arial",18))
btn_5.grid(row=3, column=2)

btn_6 = Button(root,text="6", command=Btn6, width=5,font=("Arial",18))
btn_6.grid(row=3, column=3)

btn_7 = Button(root,text="7", command=Btn7, width=5,font=("Arial",18))
btn_7.grid(row=4, column=1)

btn_8 = Button(root,text="8", command=Btn8, width=5,font=("Arial",18))
btn_8.grid(row=4, column=2)

btn_9 = Button(root,text="9", command=Btn9, width=5,font=("Arial",18))
btn_9.grid(row=4, column=3)

btn_0 = Button(root,text="0", command=Btn0, width=5,font=("Arial",18))
btn_0.grid(row=5, column=2)

# Buttons pour les opérations

btn_addition=Button(root,text="+", command=Btn_addition, width=5,font=("Arial",18))
btn_addition.grid(row=2, column=5)

btn_soustraction=Button(root,text="-", command=Btn_soustraction, width=5,font=("Arial",18))
btn_soustraction.grid(row=3, column=5)

btn_multiplication=Button(root,text="x", command=Btn_multiplication, width=5,font=("Arial",18))
btn_multiplication.grid(row=4, column=5)

btn_division=Button(root,text="/", command=Btn_division, width=5,font=("Arial",18))
btn_division.grid(row=5, column=5)

#...Buttons effacer, égale et point 

btn_egal=Button(root,text="=", command=Btn_operation, width=5,font=("Arial",18))
btn_egal.grid(row=6, column=5)

btn_effacer=Button(root,text="C", command=Btn_supprimer, width=5,font=("Arial",18))
btn_effacer.grid(row=5, column=1)

btn_dot=Button(root,text=".", command=Btn_point, width=5,font=("Arial",18))
btn_dot.grid(row=5, column=3)


root.mainloop()



