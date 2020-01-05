from datetime import date


class Ma_Date(date):
    """
    Cette classe définie une classe date qui hérite de la classe date intégrée à Python.
    Les méthodes __eq__ et __lt__ ont été surchargées. 
    """
    def __init__(self, year, month, day):
        super().__init__()

    def __eq__(self, date_to_compare):
        """
        Surcharge de l'opérateur = qui permet de comparer deux dates.
        """
        day_cmp = False
        mth_cmp = False
        yer_cmp = False
        if isinstance(date_to_compare, Ma_Date):
            if date_to_compare.day == self.day:
                day_cmp = True
            if date_to_compare.month == self.month:
                mth_cmp = True
            if date_to_compare.year == self.year:
                yer_cmp = True
        return (day_cmp and mth_cmp and yer_cmp)

    def __lt__(self, date_to_compare):
        """
        Surcharge de l'opérateur < qui permet de comparer deux dates.
        """
        day_cmp = False
        mth_cmp = False
        yer_cmp = False
        if isinstance(date_to_compare, Ma_Date):
            if date_to_compare.day < self.day:
                day_cmp = True
            if date_to_compare.month < self.month:
                mth_cmp = True
            if date_to_compare.year < self.year:
                yer_cmp = True
        return (day_cmp and mth_cmp and yer_cmp)


class Etudiant:
    """
        Classe de définition d'un étudiant

        Tests:
            >>> import ex3_class_Date
            >>> etu1 = ex3_class_Date.Etudiant("Pierre", 18)
            >>> etu1.getEmail()
            Pierre@etu.univ-tours.fr
    """
    def __init__(self, nom, age):
        self.nom = nom
        self.age_etu = age

    def email(self):
        return self.nom + "@etu.univ-tours.fr"

    def __str__(self):
        return self.nom + ", " + str(self.age_etu) + " ans"


def calcul_age(date_naiss):
    """
    Calcul de l'age d'un individu à partir de sa date de naissance.

    Args:
        date_naisse (Ma_Date) la date de naissance de l'individu
    Returns:
        (int) l'age de l'individu
    Raises:
        TypeError si le paramètre n'est pas de type Ma_Date
    """

    if isinstance(date_naiss, Ma_Date):
        today = date.today() 
        age = today.year - date_naiss.year - ((today.month, today.day) < (date_naiss.month, date_naiss.day)) 
        return age 
    return TypeError

def parse_date(date_to_parse):
    """
    Parse une date au format jj/mm/aaaa en un objet Ma_Date
    Params:
        date_to_parse (str) la date à parser au format jj/mm/aaaa
    Returns:
        Ma_Date la date parsée
    """
    jj = int(date_to_parse[0:2])
    mm = int(date_to_parse[3:5])
    aaaa = int(date_to_parse[6:10])
    return Ma_Date(aaaa, mm, jj)