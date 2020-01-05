import sqlite3
import csv
import os
import sys
from Commune import Commune, CommuneDAO
from Departement import Departement, DepartementDAO
from Region import Region, RegionDAO


FICHIER_COMMUNES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Data") + "/test_commune.csv"
FICHIER_DEPARTEMENTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Data") + "/test_dept.csv"
FICHIER_REGIONS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Data") + "/test_region.csv"

def parse_csv(csv_name):
    """ EXERCICE 1 : lecture des fichiers csv

    Cette fonction permet de lire les fichiers communes, départements et régions.csv
    Les fichiers CSV comportent des entêtes sur 8 lignes. Le parser s'en débarasse donc.

    Args:
        csv_name le nom du fichier csv à parser

    Return:
        un tableau à deux dimensions contenant pour chaque ligne une liste de champs
    """
    rows = []
    index = 0
    with open(csv_name, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        for row in csv_reader:
            index = index + 1
            # Ne pas prendre en compte les 8 premières lignes
            if index < 9:
                continue
            rows.append(row)
            #print(row)
    return rows

def peuple_table_commune(db_conn, dao, info_communes):
    """ EXERCICE 1 : Fonction de peuplement de la table Commune de la base de données

    Cette fonction permet, à partir d'un tableau à deux dimensions, de peupler
    la table Commune de la base de données. Le paramètre info_communes est une liste
    de listes contenant les informations des communes recueillies grâce à la fonction
    parse_csv().

    Args:
        info_communes ([[string]]) informations des communes
    """
    res = False
    for c in info_communes:
        commune = Commune(c[5], c[6], c[9], c[2])
        status = dao.insert(db_conn, commune)
        if status == False:
            print("Impossible d'insérer la commune " + c[5] + " dans la base")
            res = False
            break
        else:
            print("Commune "+ c[5] + " insérée dans la base")
            res = True
    return res

def peuple_table_departement(db_conn, dao, info_depts):
    """ EXERCICE 1 : Fonction de peuplement de la table Departement de la base de données

    Cette fonction permet, à partir d'un tableau à deux dimensions, de peupler
    la table Departement de la base de données. Le paramètre info_depts est une liste
    de listes contenant les informations des départements recueillies grâce à la fonction
    parse_csv().

    Args:
        info_depts ([[string]]) informations des départements
    """
    res = False
    for d in info_depts:
        dept = Departement(d[2], d[3], d[0])
        status = dao.insert(db_conn, dept)
        if status == False:
            print("Impossible d'insérer le département " + d[2] + " dans la base")
            res = False
            break
        else:
            print("Département "+ d[2] + " inséré dans la base")
            res = True
    return res

def peuple_table_region(db_conn, dao, info_regions):
    """ EXERCICE 1 : Fonction de peuplement de la table Region de la base de données

    Cette fonction permet, à partir d'un tableau à deux dimensions, de peupler
    la table Region de la base de données. Le paramètre info_regions est une liste
    de listes contenant les informations des régions recueillies grâce à la fonction
    parse_csv().

    Args:
        info_regions ([[string]]) informations des régions
    """
    res = False
    for r in info_regions:
        region = Region(r[0], r[1])
        status = dao.insert(db_conn, region)
        if status == False:
            print("Impossible d'insérer la région " + r[1] + " dans la base")
            res = False
            break
        else:
            print("Région "+ r[1] + " insérée dans la base")
            res = True
    return res

if __name__=="__main__":

    status = False
    # Connexion
    conn = sqlite3.connect("France.db")

    print("########################### EXERCICE 1 #############################")
    # Chargement des données des communes, régions et départements dans une base
    # de données nommée "France"
    ################################ COMMUNES ##################################
    commune_dao = CommuneDAO()
    # Lecture des communes
    info_communes = parse_csv(FICHIER_COMMUNES)
    # Création de la table communes
    status = commune_dao.create(conn)
    if status == False:
        print("Création table commune impossible")
    # Insertion des données des communes
    status = peuple_table_commune(conn, commune_dao, info_communes)
    if status == False:
        print("Insertion des communes impossible")

    # Validation
    if status == True:
        print("COMMIT")
        conn.commit()
        status = False
    else:
        print("ROLLBACK")
        conn.rollback()
        status = False

    ############################## DEPARTEMENTS ################################
    dept_dao = DepartementDAO()
    # Lecture des departements
    
    info_depts = parse_csv(FICHIER_DEPARTEMENTS)
    # Création de la table departements
    status = dept_dao.create(conn)
    if status == False:
        print("Création table département impossible")
    # Insertion des données des departements
    status = peuple_table_departement(conn, dept_dao, info_depts)
    if status == False:
        print("Insertion des départements impossible")

    # Validation
    if status == True:
        print("COMMIT")
        conn.commit()
        status = False
    else:
        print("ROLLBACK")
        conn.rollback()
        status = False


    ################################# REGIONS ##################################
    region_dao = RegionDAO()
    # Lecture des région
    info_regions = parse_csv(FICHIER_REGIONS)
    # Création de la table région
    status = region_dao.create(conn)
    if status == False:
        print("Création table région impossible")
    # Insertion des données des régions
    status = peuple_table_region(conn, region_dao, info_regions)
    if status == False:
        print("Insertion des régions impossible")
        
    # Validation
    if status == True:
        print("COMMIT")
        conn.commit()
        status = False
    else:
        print("ROLLBACK")
        conn.rollback()
        status = False

    print("########################### EXERCICE 2 #############################")
    # Le but est de calculer les populations des régions et des départements à
    # partir des populations entrées dans la base de données puis de les compa-
    # rer aux données des fichiers csv

    ## Calculs et affichage des populations par région
    # Parcours de la liste des régions en base
    liste_region = region_dao.read_all(conn)
    for region in liste_region:
        print("> REGION #" + str(region[0]))
        pop_region = 0
        # Parcours de la liste des départements par région
        liste_dept_de_la_region = dept_dao.read_by_region(conn, region[0])
        for dept in liste_dept_de_la_region:
            print(">> DEPARTEMENT #" + str(dept[0]))
            pop_dept = 0
            # Parcours de la liste des communes par département
            liste_commune_du_dept = commune_dao.read_by_dept(conn, dept[0])
            for commune in liste_commune_du_dept:
                #print(commune)
                pop_dept += commune[2]
            pop_region += pop_dept
            print(">> Population du département = " + str(pop_dept))
        print("> Population de la région = " + str(pop_region))

    print("########################### EXERCICE 3 #############################")
    # Le but de cet exercice est d'afficher la liste des communes ayant le même
    # nom, ainsi que les numéros de commune
    liste_communes = commune_dao.read_all(conn)
    liste_communes_meme_nom = filter(lambda x,y: x[1]==y[1], liste_communes)
    print(type(liste_communes_meme_nom))
    # for c in liste_communes_meme_nom:
    #     print(c[1])

    print("########################### EXERCICE 4 #############################")
    # Le but de cet exercice est de décharger la base de données dans un flux XML
    # mais aussi de le charger. Pour ce faire, j'utilise la librairie lxml.
    from TP5_XML import decharge_xml_communes, decharge_xml_departements, decharge_xml_regions
    from TP5_XML import charge_xml_commune
    from lxml import etree

    ## Déchargement XML
    # Communes
    liste_communes = commune_dao.read_all(conn)
    decharge_xml_communes(liste_communes)
    # Départements
    liste_departements = dept_dao.read_all(conn)
    decharge_xml_departements(liste_departements)
    # Régions
    liste_regions = region_dao.read_all(conn)
    decharge_xml_regions(liste_regions)

    # Chargement XML
    tree_communes = etree.parse("Communes.xml")
    charge_xml_commune(conn, commune_dao, tree_communes)

    # Fermeture
    conn.close()
