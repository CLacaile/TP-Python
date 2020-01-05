from lxml import etree
from Commune import Commune, CommuneDAO

def decharge_xml_communes(liste_communes):
    """ EXERICE 4: déchargement de la table Commune

    Cette fonction permet de décharger une liste de communes dans un fichier XML nommé "Communes.xml"

    Args:
        communes ([[str]]): liste des communes
    """
    # Création du noeud parent "communes"
    communes = etree.Element("communes")
    for commune_element in liste_communes:
        # Sous neoud commune
        commune = etree.SubElement(communes, "commune")
        # Attribut data_id
        commune.set("data_id", str(commune_element[0]))
        # Sous noeud nom
        nom = etree.SubElement(commune, "nom")
        nom.text = commune_element[1]
        # Sous noeud nom
        population = etree.SubElement(commune, "population")
        population.text = str(commune_element[2])
        # Sous noeud nom
        departement = etree.SubElement(commune, "departement")
        departement.text = str(commune_element[3])
    # Ecriture dans fichier Communes.xml
    communes_xml = open("Communes.xml", "wb")
    communes_xml.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
    communes_xml.write(etree.tostring(communes, pretty_print=True))
    communes_xml.close()

def decharge_xml_departements(liste_departements):
    """ EXERICE 4: déchargement de la table Departement

    Cette fonction permet de décharger une liste de départements dans un fichier XML nommé "Departements.xml"

    Args:
        liste_departements ([[str]]): liste des communes
    """
    # Création du noeud parent "departements"
    departements = etree.Element("departements")
    for departement_element in liste_departements:
        # Sous neoud departement
        departement = etree.SubElement(departements, "departement")
        # Attribut data_id
        departement.set("data_id", str(departement_element[0]))
        # Sous noeud nom
        nom = etree.SubElement(departement, "nom")
        nom.text = departement_element[1]
        # Sous noeud region
        region = etree.SubElement(departement, "region")
        region.text = str(departement_element[2])
    # Ecriture dans fichier Departements.xml
    departements_xml = open("Departements.xml", "wb")
    departements_xml.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
    departements_xml.write(etree.tostring(departements, pretty_print=True))
    departements_xml.close()

def decharge_xml_regions(liste_regions):
    """ EXERICE 4: déchargement de la table Region

    Cette fonction permet de décharger une liste de region dans un fichier XML nommé "Regions.xml"

    Args:
        liste_regions ([[str]]): liste des regions
    """
    # Création du noeud parent "regions"
    regions = etree.Element("regions")
    for region_element in liste_regions:
        # Sous neoud region
        region = etree.SubElement(regions, "region")
        # Attribut data_id
        region.set("data_id", str(region_element[0]))
        # Sous noeud nom
        nom = etree.SubElement(region, "nom")
        nom.text = region_element[1]
    # Ecriture dans fichier Communes.xml
    regions_xml = open("Regions.xml", "wb")
    regions_xml.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
    regions_xml.write(etree.tostring(regions, pretty_print=True))
    regions_xml.close()

def charge_xml_commune(db_conn, dao, etree_commmune):
    # Récupération des données et mise en forme
    communes_list = ()
    # Parcours des noeuds "Commune" du flux XML
    for node in etree_commmune.xpath("/communes/commune"):
        commune_el = ()
        # Récupération de l'attribut data_id et des valeurs des sous-élements
        for child in node.getchildren():
            commune_el += tuple([node.get("data_id")] + [child.text])
            communes_list += commune_el

    # Insertion en base
    for c in communes_list:
        commune_obj = Commune(c[0], c[1], c[3], c[5])
        dao.insert(db_conn, commune_obj)

            