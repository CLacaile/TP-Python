from random import random, randint, uniform, normalvariate
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator

def genere_int_uniforme(min, max):
    """
    Retourne un entier entre min et max selon une loi uniforme
    Args:
        min (int): la borne inférieure
        max (int): la borne supérieure
    Return:
        (int) une valeur aléatoire entre min et max 
    """

    return randint(min, max)

def genere_flt_uniform(min, max):
    """
    Retourne un float entre min et max selon une loi uniforme.
    Args:
        min (float): la borne inférieure
        max (float): la borne supérieure
    Return:
        (float) une valeur aléatoire entre min et max
    """
    return uniform(min, max)

def genere_flt_normal(moy, stdev):
    """
    Retourne un float entre min et max selon une loi normale.
    Args:
        moy (float): la moyenne de la répartition
        stdev (float): l'écart-type de la répartition
    Return:
        (float) une valeur aléatoire selon une loi normale de paramètres (moy, stdev)
    """
    return normalvariate(moy, stdev)

def plot_fig(title="Titre du graphique"):
    fig = plt.figure()
    fig.suptitle(title)

def plot_linear(var, equation, title=""):
    '''
    Draws a given equation using pyplot

    Args:
        var a numpy linspace instance
        equation the equation using var
        title the title of the graph
    '''
    plt.plot(var, equation)
    plt.title(title)

    plt.show()

def question1():
    """
    Le but de cette question est de générer un ensemble de nombres aléatoires.
    Pour cela, on fixe un nombre maximum de valeurs à générer max=500 ainsi 
    qu'une seed. 
    Ensuite, on génère des nombres suivants une loi uniforme grâce à la fonction
    genere_flt_uniform() définie dans ce module, puis des nombres suivants une loi 
    normale grâce à la fonction genere_flt_normal() définie dans ce module. Ces fon
    ctions utilisent la librairie random de Python. L'utilisation de la fonction
    numpy.linspace remplace en une seule ligne la génération de ces données.
    """
    max = 500
    seed = 100
    # Génération de nombres aléatoires
    serie_unif_X = []
    serie_unif_Y = []
    serie_norm_X = []
    serie_norm_Y = []
    for i in range(0, 2*max):
        serie_unif_X.append(i-max)
        serie_unif_Y.append(genere_flt_uniform(-max, max))
        serie_norm_X.append(i-max)
        serie_norm_Y.append(genere_flt_normal(0, 50))
    
    return serie_unif_X, serie_unif_Y, serie_norm_X, serie_norm_Y

def question2(unif_x, unif_y, norm_x, norm_y, should_plot=True):
    """
    Le but de cette question est de générer un graphique à partir
    des données générées dans la question1. Pour cela, on utilise
    les fonctions plot et show de la librairie matplotlib.
    Pour la fonction plot, le premier argument est la liste des valeurs 
    d'abscisse tandisque le second est la liste des valeurs en ordonnée.
    La fonction show() ne prend pas de paramètre.
    """
    # Génère les graphiques
    if should_plot is True:
        plt.plot(unif_x, unif_y)
        plt.plot(norm_x, norm_y)
        plt.show()

def question34(serie_unif_X, serie_unif_Y, serie_norm_X, serie_norm_Y, should_plot=True):
    """
    Le but de cette question est d'afficher plusieurs courbes avec styles et couleurs variés
    ainsi que modifier les noms des axes, la légende, ajouter des flèches pour montrer des 
    zones.

    Pour ce faire, j'ai décidé de réutiliser les 4 séries de données créés dans les 
    questions précédentes et de diviser l'affichage de la fenêtre avec 4 "sous-graphiques", 
    grâce à la fonction subplots(nb_lignes, nb_colonnes, partage_des_valeurs). Cette fonction 
    retourne un objet figure ainsi que 4 objets représentants les graphiques individuels. 
    Le paramètre de partage des valeurs en ordonnée (sharey) permet aux graphiques de fixer 
    les mêmes bornes pour les axes y (au lieu des bornes automatiques), afin de pouvoir comparer 
    plus facilement les répartitions. 
    A gauche, les graphiques portent sur les données réparties uniformément, tandis que ceux 
    de droite portent sur les données réparties normalement. 
    Pour ces répartitions, on retrouve un nuage de point créé avec la fonction 
    scatter(X, Y, couleur_marqueur, forme_marqueur) ainsi
    qu'un histogramme (hist(Y, couleur)) montrant clairement le type de répartition.
    J'ai ajouté des étiquettes fléchées avec la fonction 
    annotate(titre, position, vecteur_fleche, style_fleche), un titre par colonnes (set_title()),
    et enfin un titre principal (suptitle()).
    """
    if should_plot is True:
        # Subplots: création de l'affichage divisé en 4
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharey='row')
        # Colonne répartition uniforme
        ax1.scatter(serie_unif_X, serie_unif_Y, c='red', marker='+')
        ax1.annotate("Répartition uniforme", xy=(-400, 0), xytext=(-500, 200),
                        arrowprops=dict(arrowstyle="->"))
        ax1.set_title("Valeurs uniformément réparties")
        ax3.hist(serie_unif_Y, color='red')
        # Colonne répartition normale
        ax2.scatter(serie_norm_X, serie_norm_Y, marker='x')
        ax2.annotate("Répartition normale", xy=(200, 0), xytext=(200, 200),
                        arrowprops=dict(arrowstyle="->"))
        ax2.set_title("Valeurs normalement réparties")
        ax4.hist(serie_norm_Y)
        # Titre + affichage
        fig.suptitle("Etude des distributions uniformes et normales")
        plt.show()

def question5(should_plot=True):
    """
    Le but de cette question est d'afficher un camembert (l'histogramme a déjà été traité 
    dans la question précédente).

    On crée une liste de 4 parts aléatoires selon une loi uniforme entre 0 et 25% ainsi
    qu'une liste de noms des parts qui seront affichés sur le camembert.
    Ensuite, on utilise la fonction pie(parts, noms)
    """
    # Camembert
    if should_plot is True:
        parts = [randint(0,25), randint(0,25), randint(0,25), randint(0,25)]
        labels = ["Voitures", "Camions", "Avions", "Bateaux"]
        plt.pie(parts, labels=labels, autopct='%1.1f%%')
        plt.show()

def question6(should_plot=True):
    """
    Le but de cette question est d'afficher une surface 2D dans un espace 3D (mesh).
    Pour cela, on génère des valeurs entre -5 et 5 pour deux vecteurs : X et Y 
    en utilisant la fonction linspace issue de numpy. Ensuite on créé deux matrices
    de coordonnées à partir des vecteurs X et Y en utilisant la fonction numpy.meshgrid.
    Enfin on créé la matrice des valeurs que l'on veut tracer : ici on a choisi de tracer
    la fonction $\sqrt{X^2+Y^2}$.
    Enfin, on trace la forme dans un graphique 3D en utilisant les valeurs généres précé-
    demment.
    """
    if should_plot == False:
        return
    X = np.linspace(-5,5,40)
    Y = np.linspace(-5,5,40)
    X,Y = np.meshgrid(X,Y)
    Z = np.sqrt(X**2+Y**2)
    plt.gca(projection='3d').plot_surface(X,Y,Z.T)
    plt.show()

if __name__ == "__main__":
    
    # Question 1
    print("========== QUESTION 1 ==========")
    unif_x, unif_y, norm_x, norm_y = question1()
    # Question 2
    print("========== QUESTION 2 ==========")
    question2(unif_x, unif_y, norm_x, norm_y, should_plot=False)
    # Question 3 et 4
    print("========== QUESTION 3 et 4 ==========")
    question34(unif_x, unif_y, norm_x, norm_y, should_plot=False)
    # Question 5
    print("========== QUESTION 5 ==========")
    question5(should_plot=False)
    # Question 6
    print("========== QUESTION 6 ==========")
    question6(should_plot=True)

    