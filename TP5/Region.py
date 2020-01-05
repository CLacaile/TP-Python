import sqlite3

class Region:
    """ 
    Cette classe représente un région

    Attr:
        _code_region (int): code de la région, sert de PK
        _nom_region (string): nom de la région
    """
    def __init__(self, code_region, nom_region):
        self._code_region = code_region
        self._nom_region = nom_region

    def __str__(self):
        return "#" + self._code_region + " " + self._nom_region

class RegionDAO:
    def create(self, db_conn):
        sql = '''CREATE TABLE region (
                    id_region         INT CONSTRAINT pk_region PRIMARY KEY,
                    nom_region        CHARACTER(30)
                    );'''
        try:
            db_conn.execute(sql)
        except sqlite3.OperationalError:
            print("RegionDAO.create: sqlite3.OperationalError")
            return False
        else:
            print("Table Region créée")
            return True
    
    def insert(self, db_conn, region):
        if isinstance(region, Region) == False:
            raise TypeError
        sql = "INSERT INTO region VALUES (?, ?);"
        values = (region._code_region, region._nom_region)
        try:
            db_conn.execute(sql, values)
        except sqlite3.OperationalError:
            print("RegionDAO.insert: sqlite3.OperationalError")
            return False
        except sqlite3.IntegrityError:
            print("RegionDAO.insert: sqlite3.IntegrityError, violation de contrainte d'unicité")
            return False
        else:
             return True

    def delete(self, db_conn, code_region):
        sql = ''' DELETE FROM region
                  WHERE id_region = ?'''
        try:
            db_conn.execute(sql, (code_region,))
        except sqlite3.OperationalError:
            print("RegionDAO.delete: sqlite3.OperationalError")
            return   

    def read(self, db_conn, code_region):
        sql = ''' SELECT * 
                  FROM region
                  WHERE id_region = ? '''
        try:
            res = db_conn.execute(sql, (code_region,))
        except sqlite3.OperationalError:
            print("RegionDAO.read: sqlite3.OperationalError")
            return 
        else:
            return res
    
    def read_all(self, db_conn):
        sql = ''' SELECT * 
                  FROM region '''
        curs = db_conn.cursor()
        try:
            curs.execute(sql)
            res = curs.fetchall()
        except sqlite3.OperationalError:
            print("RegionDAO.read_all: sqlite3.OperationalError")
            return 
        else:
            return res

    def update(self, db_conn, code_region, nom_region):
        sql = ''' UPDATE region
                    SET nom_region = ?,
                    WHERE id_region = ?;'''
        values = (nom_region, (code_region,))
        try:
            db_conn.execute(sql, values)
        except sqlite3.OperationalError:
            print("RegionDAO.update: sqlite3.OperationalError")
            return False
        else:
            return True
