import os

menu_dict = {"1": "Choisir un nom de fichier à ouvrir",
             "2": "Ajouter un texte",
             "3": "Afficher le fichier",
             "4": "Vider le fichier",
             "9": "Quitter"}


def editor_main():
    """ File editor main function
    
    This function is the main function for editing a file. 
    It displays the menu defined by the dictionary menu_dict
    using print_dict(), takes the input of a user using 
    input_menu() and process the command like following:
    1: load the filename of the file to edit
    2: add a new line to the file
    3: show the content of the file
    4: overwrite the file
    9: quit the program

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
    """ Function that prints a dictionary

    This functions prints a dictionary.

    Param:
        dict (Dictionary): the dictionary to print
    
    Examples:
        >>> print_dict({"1": "Hello,", "2": "world!"})
        1 : Hello,
        2 : world!

    """
    for k in dict.keys():
        print(k + " : " + dict[k])


def input_menu():
    """ Function that prints out "Entrez un choix" 
    and returns the string input by the user. It uses
    the keys of the global dictionary to determine 
    if the input is valid or not.

    Return:
        string: the string input by the user
        
    """
    choix = input(">>> Entrez un choix : ")
    while choix not in menu_dict.keys():
        choix = input(">>> Entrez un choix valide : ")
    return choix


def load_file(file_name):
    """ File loading function

    Open the file in write mode and place the cursor at the end (append).
    If the file doesn't exist, it creates it.

    Args:
        file_name (str): the name of the file to open or create

    Returns:
        file: the file opened

    """
    file_loaded = open(file_name, "a")
    return file_loaded

# Launch editor_main() as soon as this file is called
if __name__ == "__main__":
    editor_main()
