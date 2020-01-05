import os
import getpass
from bcrypt import hashpw, gensalt, checkpw

menu_dict = {"1": "Choisir un nom de fichier à ouvrir",
             "2": "Ajouter un texte",
             "3": "Afficher le fichier",
             "4": "Vider le fichier",
             "5": "Créer un utilisateur",
             "9": "Quitter"}

def exercice1():
    """ Fonction principale de l'exercice 1 : éditeur de fichiers
    
    Le but de cet exercice est de proposer un outil de gestion de fichier sécurisé
    qui reprend les fonctionnalités développées au TP1, en y ajoutant une authentification
    et la gestion d'exceptions.
    """
    # Variables
    name_of_file = None
    run_flag = True

    # Login
    print("===== CONNEXION =====")
    if login() is False:
        print("Utilisateur ou mot de passe incorrect")
        login()

    # Text editor
    print("===== EDITEUR DE TEXTE =====")
    while run_flag is True:
        
        # Show the menu
        print_dict(menu_dict)
        choix = input_menu()

        # Loading of the file
        if choix == "1":
            name_of_file_to_check = input(">>> Entrez un nom de fichier : ")
            try:
                ctrl_filename(name_of_file_to_check)
            except AssertionError:
                print("!!! Le nom du fichier n'est pas une chaîne de caractère")
            except ValueError:
                print("!!! Le nom du fichier est vide")
            else:
                name_of_file = name_of_file_to_check
        # Appending some text
        elif choix == "2":
            text = input(">>> Entrez le texte à ajouter au fichier : ")
            try:
                append_text(name_of_file, text)
            except AssertionError:
                print("!!! Au moins un des paramètres saisis n'est pas une chaine de caractère")
            else:
                print(">>> Ligne ajoutée")
            
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
        elif choix == "5":
            create_user()
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

def ctrl_filename(file_name):
    assert type(file_name) == str
    if not file_name.strip():
        raise ValueError

def append_text(name_of_file, text):
    assert type(name_of_file) == str
    assert type(text) == str 
    try:
        with open(name_of_file, "a") as file_to_edit:
            file_to_edit.write(text + '\n')
        file_to_edit.close()
    except FileExistsError:
        print("!!! Le fichier est déjà ouvert en mode création exclusive")

def login():
    """ Fonction de connexion

    Demande à l'utilisateur un nom et un mot de passe et vérifie que le couple est bien présent dans le fichier "users".

    Returns:
        True si le couple est bien présent dans le fichier "users", False sinon

    """
    is_auth = False
    user = input("User: ")
    pswd = getpass.getpass()
    try:
        with open("users", "r") as usersfile:
            file_content = usersfile.readlines()
            for num_line in range(len(file_content)):
                if file_content[num_line] == (user+pswd):
                    is_auth = True
            usersfile.close()
    except: 
        print("!!! Impossible d'ouvrir le fichier des utilisateurs")
    finally:
        return is_auth

def create_user():
    """ Fonction de création d'un utilisateur 

    Demande à un utilisateur d'entrer un nom et un mot de passe du nouvel utilisateur à créer puis l'ajoute au fichier 
    "users" en le hashant. Si le fichier n'existe pas, il est créé.
    """
    user = input("User: ")
    pswd = getpass.getpass()
    try:
        with open("users", "a") as usersfile:
            usersfile.write(user+hash_password(pswd))
    except: 
        print("!!! Impossible d'ouvrir le fichier des utilisateurs")
    else:
        print(">>> L'utilisateur "+user+ " a été créé.")

def hash_password(password_to_hash):
    """
    Hashage du password
    """
    return hashpw(password_to_hash, gensalt())


# Launch editor_main() as soon as this file is called
if __name__ == "__main__":
    exercice1()
