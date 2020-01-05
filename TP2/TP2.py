from tkinter import *
from math import *


expression = "" 

def press(num):
    """ Fonction de gestion de la pression d'un bouton de valeur "num"

    Cette fonction permet de gérer l'appui d'un touche (sauf "=", Clear et Del).
    Elle met à jour le contenu de l'afficheur.
    Args:
        num (str) la touche pressée
    """
    global expression 
    expression = expression + str(num) 
    equation.set(expression)
    print(expression)


def equalpress():
    """ Fonction de gestion du bouton "="

    Cette touche permet de gérer le comportement du bouton "=".
    Elle évalue le contenu de la saisie avec la fonction eval()
    puis affiche le résultat dans l'afficheur. Si une exception
    est levée (par exemple en cas de division par zéro), l'afficheur
    prend la valeur ERROR et le buffer est vidé.
    """
    try: 
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        print(total)
        expression = total
    except: 
        equation.set("ERROR") 
        expression = "" 

def delpress():
    """ Fonction de gestion du bouton "Del"

    Cette fonction permet de gérer le comportement du bouton "Del".
    Il permet d'effacer le dernier caractère saisi par l'utilisateur.
    Elle met à jour l'afficheur en conséquence.
    """
    global expression
    expression = expression[:-1]
    equation.set(expression)

def clear(): 
    """ Fonction de gestion du bouton "Clear"

    Cette fonction permet de vider complètement le buffer.
    Elle met à jour l'afficheur en conséquence.
    """
    global expression 
    expression = "" 
    equation.set("") 



if __name__ == "__main__":  
    window = Tk() 
    window.title("Calculatrice") 
    window.geometry("400x300") 

    # Définition de la taille des colonnes et lignes pour l'affichage
    for row in range(1,7):
        window.rowconfigure(row, weight=1)
        window.columnconfigure(row, weight=1)

    # Variables d'affichage
    equation = StringVar()
    equation.set('enter your expression') 

    # Afficheur
    expression_field = Label(window, textvariable=equation)
    expression_field.grid(row = 1, column = 1, columnspan = 5)

    # Boutons numériques
    # Pour éviter d'avoir à créer une fonction pour chaque bouton, j'ai créé une fonction press(num) qui sera appelée 
    # via une fonction lambda : le paramètre command prend un objet fonction, on ne peut pas lui associer de paramètre,
    # d'où l'emploi de la fonction lambda
    button1 = Button(window, text=' 1 ', command=lambda: press(1)) 
    button1.grid(row = 5, column = 1, sticky='nesw')

    button2 = Button(window, text=' 2 ', command=lambda: press(2)) 
    button2.grid(row = 5, column = 2, sticky='nesw')

    button3 = Button(window, text=' 3 ', command=lambda: press(3)) 
    button3.grid(row = 5, column = 3, sticky='nesw') 

    button4 = Button(window, text=' 4 ', command=lambda: press(4)) 
    button4.grid(row = 4, column = 1, sticky='nesw')

    button5 = Button(window, text=' 5 ', command=lambda: press(5)) 
    button5.grid(row = 4, column = 2, sticky='nesw')

    button6 = Button(window, text=' 6 ', command=lambda: press(6)) 
    button6.grid(row = 4, column = 3, sticky='nesw')

    button7 = Button(window, text=' 7 ', command=lambda: press(7)) 
    button7.grid(row = 3, column = 1, sticky='nesw')

    button8 = Button(window, text=' 8 ', command=lambda: press(8)) 
    button8.grid(row = 3, column = 2, sticky='nesw')

    button9 = Button(window, text=' 9 ', command=lambda: press(9)) 
    button9.grid(row = 3, column = 3, sticky='nesw')

    button0 = Button(window, text=' 0 ', command=lambda: press(0)) 
    button0.grid(row = 6, column = 2, sticky='nesw')

    # Opérateurs
    plus = Button(window, text=' + ', command=lambda: press("+")) 
    plus.grid(row = 4, column = 4, sticky='nesw')

    minus = Button(window, text=' - ', command=lambda: press("-")) 

    multiply = Button(window, text=' x ', command=lambda: press("*"))
    multiply.grid(row = 5, column = 4, sticky='nesw')

    divide = Button(window, text=' / ', command=lambda: press("/"))
    divide.grid(row = 3, column = 4, sticky='nesw')

    equal = Button(window, text=' = ', command=equalpress)
    equal.grid(row = 6, column = 4, sticky='nesw')

    power2 = Button(window, text='²', command=lambda:press("**2"))
    power2.grid(row = 4, column = 5, sticky='nesw')

    powerX = Button(window, text='^', command=lambda:press("**"))
    powerX.grid(row = 3, column = 5, sticky='nesw')

    # Parenthèses
    open_parenthesis = Button(window, text=' ( ', command=lambda: press("("))
    open_parenthesis.grid(row = 2, column = 1, sticky='nesw')

    close_parenthesis = Button(window, text=' ) ', command=lambda: press(")"))
    close_parenthesis.grid(row = 2, column = 2, sticky='nesw')

    # Trigo
    cosine = Button(window, text=' cos ', command=lambda: press("cos"))
    cosine.grid(row = 2, column = 3, sticky='nesw')

    sinus = Button(window, text=' sin ', command=lambda: press("sin"))
    sinus.grid(row = 2, column = 4, sticky='nesw')

    tang = Button(window, text=' tan ', command=lambda: press("tan"))
    tang.grid(row = 2, column = 5, sticky='nesw')

    # Décimales
    coma = Button(window, text=' . ', command=lambda:press("."))
    coma.grid(row=6, column=3, sticky='nesw')

    # Gestion buffer
    clearall = Button(window, text='Clear', command=clear)
    clearall.grid(row = 5, column = 5, sticky='nesw')

    delete = Button(window, text='Del', command=delpress)
    delete.grid(row = 6, column = 5, sticky='nesw')

    # boucle principale
    window.mainloop() 
