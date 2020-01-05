import os

################################# EXERCICE 1 ###################################
def exercice1():
    """
    Le but de cet exercice est d'afficher "Hello, world!" dans la console
    """
    print("Hello, world!")

################################# EXERCICE 2 ###################################
menu_dict = {"1": "Choisir un nom de fichier à ouvrir",
             "2": "Ajouter un texte",
             "3": "Afficher le fichier",
             "4": "Vider le fichier",
             "9": "Quitter"}


def exercice2():
    """ Fonction principale de l'exercice 2 : éditeur de fichiers

    Le but de cet exercice est de proposer un outil de gestion de fichier au tra
    vers d'un menu console tel que : 
        1. Charger le fichier
        2. Ajouter du texte au fichier
        3. Lire le fichier chargé
        4. Vider le fichier
        5. Quitter l'outil

    Pour ce faire, j'ai d'abord créé un drapeau (run_flag) à Vrai qui permet, lorsqu'il passe
    à Faux (par l'option 5), de quitter le programme. Ensuite, pour l'option 1, 
    le chargement du fichier ne charge en fait que le nom du fichier, mais n'uti
    lise pas de open(). Cette fonction est seulement utilisée pour l'option 2, 3,
    ou 4, afin de spécifier le mode de lecture/écriture du fichier. En 2 (ajout
    de texte à la fin du fichier), l'option vaut "a", et les lignes sont ajoutées
    avec la fonction write(). En 3 (lecture du fichier), le fichier est ouvert
    avec l'option "r", et lu avec la fonction readlines(). Enfin, en 4, l'open()
    est utilisé avec l'option "w". A la fin de chacune de ces options, le fichier
    est fermé avec la fonction close().
    """
    # Variables
    name_of_file = None
    run_flag = True

    # Processing
    print("===== EDITEUR DE TEXTE =====")
    while run_flag is True:
        #print_menu()
        print_dict(menu_dict)
        choix = input_menu()

        # Loading of the file
        if choix == "1":
            name_of_file = input(">>> Entrez un nom de fichier : ")
        # Appending some text
        elif choix == "2":
            # TODO: take care of blank name_of_file
            if name_of_file is not None:
                text = input(">>> Entrez le texte à ajouter au fichier : ")
                with open(name_of_file, "a") as file_to_edit:
                    file_to_edit.write(text + '\n')
                file_to_edit.close()
            else:
                print("!!! Veuillez charger un nom de fichier valide")
        # Reading the file
        elif choix == "3":
            # TODO: take care of blank name_of_file
            if name_of_file is not None:
                with open(name_of_file, "r") as file_to_read:
                    file_content = file_to_read.readlines()
                    for num_line in range(len(file_content)):
                        print(file_content[num_line])
                file_to_read.close()
            else:
                print("!!! Veuillez ouvrir un fichier")
        # Overwriting the file
        elif choix == "4":
            # TODO: take care of blank name_of_file
            if name_of_file is not None:
                file_to_overwrite = open(name_of_file, "w")
                file_to_overwrite.close()
            else:
                print("!!! Veuillez ouvrir un fichier")
        # Quit
        elif choix == "9":
            run_flag = False


def print_dict(dict):
    """
    Cette fonction imprime un dictionnaire dans la console

    Param:
        dict (Dictionary): the dictionary to print
    
    Example:
        >>> print_dict({"1": "Hello,", "2": "world!"})
        1 : Hello,
        2 : world!
    """
    for k in dict.keys():
        print(k + " : " + dict[k])


def input_menu():
    """ 
    Cette fonction imprime "Entrez un choix" dans la console et retourne la chai
    ne saisie par l'utilisateur. Elle vérifie que l'entrée est conforme au dicti
    onnaire défini gloabelement en début de fichier.

    Return:
        string: the string input by the user
    """
    choix = input(">>> Entrez un choix : ")
    while choix not in menu_dict.keys():
        choix = input(">>> Entrez un choix valide : ")
    return choix


def load_file(file_name):
    """ 
    Cette fonction charge un fichier en mode écriture et place le curseur à la f
    in. Si le fichier n'existe pas, il est créé.

    Args:
        file_name (str): the name of the file to open or create

    Returns:
        file: the file opened
    """
    file_loaded = open(file_name, "a")
    return file_loaded

################################# EXERCICE 3 ###################################
from ex3_class_Date import Ma_Date, Etudiant, calcul_age, parse_date
from datetime import date
import csv

def exercice3A():
    """
    Le but de cet exercice est de créer une classe date et de surcharger les opé
    rateurs = et <.
    """
    date1 = Ma_Date(2020, 1, 1)
    date2 = Ma_Date(2019, 12, 1)
    nouvel_an = Ma_Date(2020, 1, 1)
    if date1 == nouvel_an:
        print("C'est le nouvel an ! Bonne année")
    else:
        if date1.__lt__(nouvel_an):
            print("Ce n'est pas encore le nouvel an, patience !")
        else:
            print("Le nouvel an est déjà passé, trop tard !")

def exercice3B():
    """
    Le but de cet exercice est de créer une classe Etudiant et de pouvoir charger
    des objets à partir d'un fichier CSV.
    Comme dans l'exercice 1, on ouvre le fichier CSV avec la fonction open(). Ensuite,
    on utilise un csv.reader() pour lire les lignes et les colonnes (séparées par des ;).
    Pour chaque ligne du fichier, on ajoute à la liste des étudiants un nouvel étudiant
    dont l'age a été parsée a partir d'une date de naissance puis calculée.
    Enfin, on imprime à l'écran le dernier étudiant inséré, puis le nombre de ligne traitées.
    """
    etudiants = []
    # Read the CSV
    with open('fichetu.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            etudiants.append(Etudiant(row[1] + " " + row[0], calcul_age(parse_date(row[2]))))
            print(etudiants[-1])
            line_count += 1
        print(line_count + " lignes traitées")

################################### MAIN ######################################
if __name__=="__main__":
    print("=============== Exercice 1 ================")
    exercice1()
    print("=============== Exerice 2 =================")
    exercice2()
    print("============ Exerice 3 : date =============")
    exercice3A()
    print("========== Exerice 3 : etudiant ===========")
    exercice3B()
