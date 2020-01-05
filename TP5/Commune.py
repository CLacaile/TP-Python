import sqlite3

class Commune:
    """ 
    Cette classe représente une commune

    Attr:
        _code_commune (int): l'identifiant commune (PK)
        _nom_commune (str): le nom de la commune
        _pop_totale (int): le nombre d'habitants
        _code_dept (int): pseudo clé étrangère sur les département
    """
    def __init__(self, code_commune, nom_commune, pop_totale, code_dept):
        self._code_commune = code_commune
        self._nom_commune = nom_commune
        self._pop_totale = pop_totale
        self._code_dept = code_dept

    def __str__(self):
        return "#" + self._code_commune + " " + self._nom_commune + " : " + self._pop_totale

class CommuneDAO:
    """
    Cette classe permet de créer la table "commune" dans la base de données, mais aussi d'insérer un élément, 
    supprimer un élément, lire un élément, lire un élément selon son département, lire tous les éléments de
    la table et enfin mettre à jour un élément.
    """
    def create(self, db_conn):
        """ Fonction de création de la table "commune" dans la base spécifiée par l'argument db_conn

        Args:
            db_conn (Connection) objet de connexion à la base de données

        Return:
            True si la création s'est effectuée correctement, False sinon
        """
        sql = '''CREATE TABLE commune (
                    id_commune      INT CONSTRAINT pk_commune PRIMARY KEY,
                    nom_commune     CHARACTER(100),
                    pop_totale      INT,
                    code_dept       INT
                    );'''
        try:
            db_conn.execute(sql)
        except sqlite3.OperationalError:
            print("CommuneDAO.create: sqlite3.OperationalError")
            return False
        else:
            return True
    
    def insert(self, db_conn, commune):
        """ Fonction d'insertion d'un objet Commune dans la base de données

        Args:
            db_conn (Connection) objet de connexion à la base de données
            commune (Commune) objet à insérer dans la base de données
        Return:
            True si l'insertion s'est correctement déroulée, False sinon
        """
        if isinstance(commune, Commune) == False:
            raise TypeError
        sql = "INSERT INTO commune VALUES (?, ?, ?, ?);"
        values = (commune._code_commune, commune._nom_commune, commune._pop_totale, commune._code_dept)
        try:
            db_conn.execute(sql, values)
        except sqlite3.OperationalError:
            print("CommuneDAO.insert: sqlite3.OperationalError")
            return False
        except sqlite3.IntegrityError:
            print("CommuneDAO.insert: sqlite3.IntegrityError, violation de contrainte d'unicité")
            return False
        else:
             return True

    def delete(self, db_conn, code_commune):
        """ Fonction de suppression d'un élément dans la base de données

        Args:
            db_conn (Connection) objet de connexion à la base de données
            code_commune (int) identifiant de l'objet à supprimer
        Return:
            True si la suppression s'est correctement déroulée, False sinon
        """
        sql = ''' DELETE FROM commune
                  WHERE id_commune = ?'''
        try:
            db_conn.execute(sql, (code_commune,))
        except sqlite3.OperationalError:
            print("CommuneDAO.delete: sqlite3.OperationalError")
            return False
        else:
            return True

    def read(self, db_conn, code_commune):
        """ Fonction de lecture d'un élément dans la base de données

        Cette fonction permet de lire un élément "Commune" dans la base de 
        données en fonction de son code_commune, identifiant primaire de la 
        table. Il est important de noter que cette fonction fait appel à la 
        méthode cursor.fetchall()qui renvoie une liste d'éléments répondant à la
        clause WHERE spécifiée dans la requête.
        L'utilisation de cursor.fetchone() n'a pas été jugée prudente.
        Ici, puisque code_commune est l'identifiant unique de la table, la liste 
        retrounée contiendra toujours au plus 1 élément.

        Args:
            db_conn (Connection) objet de connexion à la base de données
            code_commune (int) identifiant de l'objet à lire
        Return:
            (list) liste d'éléments vérifiants le code_commune, None sinon
        """
        sql = ''' SELECT * 
                  FROM commune
                  WHERE id_commune = ?'''
        curs = db_conn.cursor()
        try:
            curs.execute(sql, (code_commune,))
            res = curs.fetchall()
        except sqlite3.OperationalError:
            print("CommuneDAO.read: sqlite3.OperationalError")
            return 
        else:
            return res

    def read_by_dept(self, db_conn, code_dept):
        """ Fonction de lecture d'un élément dans la base de données

        Cette fonction permet de lire un élément "Commune" dans la base de 
        données en fonction de son code_dept. 

        Args:
            db_conn (Connection) objet de connexion à la base de données
            code_dept (int) identifiant du département de l'objet à lire
        Return:
            (list) liste d'éléments vérifiants le code_dept, None sinon
        """
        sql = ''' SELECT * 
                  FROM commune
                  WHERE code_dept = ?'''
        curs = db_conn.cursor()
        try:
            curs.execute(sql, (code_dept,))
            res = curs.fetchall()
        except sqlite3.OperationalError:
            print("CommuneDAO.read_by_dept: sqlite3.OperationalError")
            return
        else:
            return res
    
    def read_all(self, db_conn):
        """ Fonction de lecture de tous les éléments dans la base de données

        Cette fonction permet de lire tous les éléments "Commune" dans la base 
        de données.

        Args:
            db_conn (Connection) objet de connexion à la base de données
        Return:
            (list) liste d'éléments, None si aucun élément n'est présent dans la
            base.
        """
        sql = ''' SELECT * 
                  FROM commune '''
        curs = db_conn.cursor()
        try:
            curs.execute(sql)
            res = curs.fetchall()
        except sqlite3.OperationalError:
            print("CommuneDAO.read_all: sqlite3.OperationalError")
            return 
        else:
            return res

    def update(self, db_conn, code_commune, nom_commune, pop_totale, code_dept):
        """ Fonction de mise à jour d'un élément dans la base de données

        Args:
            db_conn (Connection) objet de connexion à la base de données
            code_commune (int) identifiant de l'objet à màj
            nom_commune (str) nom de l'objet à màj
            pop_totale (int) pop.totale de l'objet à màj
            code_dept (int) code département de l'objet à màj
        """
        sql = ''' UPDATE commune
                    SET nom_commune = ?,
                        pop_totale = ?,
                        code_dept = ?
                    WHERE id_commune = ?;'''
        values = (nom_commune, pop_totale, code_dept, code_commune)
        try:
            db_conn.execute(sql, values)
        except sqlite3.OperationalError:
            print("CommuneDAO.update: sqlite3.OperationalError")
            return False
        else:
            return True
