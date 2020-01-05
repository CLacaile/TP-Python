import numpy as np
from scipy.optimize import curve_fit
from scipy import ndimage
import matplotlib.pyplot as plt
from math import exp

def question1():
    """
    Le but de la question est de créer un tableau de dimension 3
    avec un shape de (4, 3, 2) remplit avec des nombres aléatoires.
    
    Pour y répondre, on génère d'abord un tableau de 24 nombres aléatoires
    à l'aide de la fonction numpy.randint(). Ensuite, on les ré-arrange dans un 
    tableau à trois dimensions avec la fonction numpy.reshape(4,3,2). Enfin,
    on affiche ses attributs ndim, shape, size, dtype, itemsize, data.
    """
    # Génération des nombres aléatoires
    arr = np.random.randint(low=1, high=10, size=24)
    # Tableau 3D
    arr = arr.reshape(4,3,2)
    # Attributs
    print("Nombre de dimensions: ", arr.ndim)
    print("Taille des dimensions (x,y,z): ", arr.shape)
    print("Nombre d'éléments: ", arr.size)
    print("Type des éléments: ", arr.dtype)
    print("Taille des éléments: ", arr.itemsize)
    print("Données: ", arr.data)

    return arr

def question2():
    """
    Le but de la question est de créer 2 matrices 3x3 initialisées avec
    les entiers de 0 à 8 pour la 1e et de 2 à 10 pour la 2e puis calculer
    le produit des 2 (différence entre * et dot). Transposer une matrice.

    On génère les valeurs des deux matrices m1 et m2 à l'aide de la fonction 
    linspace() puis on forme les dimensions avec reshape(). On calcule
    ensuite le produit terme à terme des deux matrices avec l'opérateur '.'.
    On transpose ensuite la matrice issue de m1.dot(m2)
    """
    m1 = np.linspace(start=0, stop=8, num=9)
    m1 = m1.reshape(3,3)
    print("Matrice m1 = \n", m1)
    m2 = np.linspace(start=2, stop=10, num=9)
    m2 = m2.reshape(3,3)
    print("Matrice m2 = \n", m2)
    # Multiplication
    terme_a_terme = m1*m2
    print("Multiplication terme à terme m1*m2= \n", terme_a_terme)
    mult = m1.dot(m2)
    print("Multiplication m1.dot(m2) = \n", mult)
    # Transposition
    transp = mult.transpose()
    print("Transposée de m1.dot(m2) = \n", transp)

def question3():
    """
    Cette question a pour but de calculer le déterminant et l’inverse d’une matrice,
    résoudre un système d’équations linéaires, puis calculer les valeurs et vecteurs
    propres d’une matrice.

    D'abord, on instancie une matrice m1 telle que : 
    m1 = [[10, 9, 1], [9, 10, 5], [1, 5, 9]]
    Ensuite, on calcule son déterminant à l'aide de la fonction np.linalg.det puis 
    son inverse à l'aide de la fonction np.linalg.inv.
    Ensuite, on résoud le système m1 = [-50, 40, 180] à l'aide de np.linalg.solve.
    Enfin, on détermine les valeurs et vecteurs propres de m1 avec la fonction 
    np.linalg.eig(m1)
    """
    # Création matrice de travail
    m1 = np.array([[10, 9, 1], [9, 10, 5], [1, 5, 9]])
    print("Matrice M1 = \n", m1)
    # Calcul du déterminant
    det = np.linalg.det(m1)
    inv = np.linalg.inv(m1)
    print("Déterminant = ", det)
    print("Inversion = \n", inv)
    # Résolution du système
    m2 = np.array([-50, 40, 180])
    res = np.linalg.solve(m1,m2)
    print("Résolution du système m1 = [-50, 40, 180] => ", res)
    # Valeurs et vecteurs propres
    eig_m1 = np.linalg.eig(m1)
    print("Valeurs propres de m1 = ", eig_m1[0])
    print("Vecteurs propres de m1 = \n", eig_m1[1])

def question4_exp_test(T, A):
    return A*np.exp(1/T)

def question4(should_plot=True):
    """
    Le but de cette question est d'pprocher un ensemble de points par une 
    courbe (optimize.curve_fit ou interpolate.interp1d).

    On génère d'abord un ensemble de points suivants une loi exponentielle
    avec une "marge" aléatoire uniforme de + ou - 0.5, puis on affiche ces
    points dans un nuage avec matplotlib. Ensuite, on fit la courbe avec
    la fonction scipy.optimisze.curve_fit. Cette fonction prend comme 
    paramètres la fonction dont les paramètres sont à fitter (ici, une fonction
    exponentielle tq f(T) = A*exp(1/T)) ainsi que les données à partir desquelles
    fitter la courbe. Enfin, on affiche la courbe sur un graphe.

    """
    
    # Abscisse
    x = np.linspace(1, 10, num=50)
    # Ordonnée
    y = np.exp(1/x) + np.random.uniform(low=-0.5, high=0.5, size=50)
    # Nuage de points des données x et y
    if should_plot is True:
        plt.scatter(x, y, c='red', marker='+', label='Data to fit')
    # Curve fitting
    params, params_covariance = curve_fit(question4_exp_test, x, y)
    print(params)
    # Trace du fit
    if should_plot is True:
        plt.plot(x, question4_exp_test(x, params[0]), label='Fitted function')
        plt.annotate("A = "+str(params[0]), xy=(2.5,2))
        plt.legend(loc="best")
        plt.title(label="Question 4 : curve fitting")
        plt.show()

def question5():
    """
    Le but de cette question est de lire une image jpeg et afficher l’image
    originale et réduite en taille.
    Cette question n'est pas traitée.
    """




if __name__=="__main__":
    ## PARTIE 1 : NUMPY
    # Question 1
    print("========== QUESTION 1 ==========")
    question1()
    # Question 2
    print("========== QUESTION 2 ==========")
    question2()
    # Question 3
    print("========== QUESTION 3 ==========")
    question3()

    ## PARTIE 2 : SCIPY
    print("========== QUESTION 4 ==========")
    question4()
    print("========== QUESTION 5 ==========")
    question5()


