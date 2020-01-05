import sqlite3

class Departement:
    """ 
    Cette classe représente un département

    Attr:
        _code_dept (int): code du département, sert de PK
        _nom_dept (string): nom du département
        _code_region (int): code de la région à laquelle appartient le départment
    """
    def __init__(self, code_dept, nom_dept, code_region):
        self._code_dept = code_dept
        self._nom_dept = nom_dept
        self._code_region = code_region

    def __str__(self):
        return "#" + self._code_dept + " " + self._nom_dept + ", région: " + self._code_region

class DepartementDAO:
    def create(self, db_conn):
        sql = '''CREATE TABLE departement (
                    id_dept         INT CONSTRAINT pk_departement PRIMARY KEY,
                    nom_dept        CHARACTER(30),
                    code_region     INT
                    );'''
        try:
            db_conn.execute(sql)
        except sqlite3.OperationalError:
            print("DepartementDAO.create: sqlite3.OperationalError")
            return False
        else:
            return True
    
    def insert(self, db_conn, departement):
        if isinstance(departement, Departement) == False:
            raise TypeError
        sql = ''' INSERT INTO departement VALUES(?, ?, ?);'''
        values = (departement._code_dept, departement._nom_dept, departement._code_region)
        try:
            db_conn.execute(sql, values)
        except sqlite3.OperationalError:
            print("DepartementDAO.insert: sqlite3.OperationalError")
            return False
        except sqlite3.IntegrityError:
            print("DepartementDAO.insert: sqlite3.IntegrityError, violation de contrainte d'unicité")
            return False
        else:
            return True

    def delete(self, db_conn, code_dept):
        sql = ''' DELETE FROM departement
                  WHERE id_dept = ?'''
        try:
            db_conn.execute(sql, (code_dept,))
        except sqlite3.OperationalError:
            print("DepartementDAO.delete: sqlite3.OperationalError")
            return   

    def read(self, db_conn, code_dept):
        sql = ''' SELECT * 
                  FROM departement
                  WHERE id_dept = ? '''
        curs = db_conn.cursor()
        try:
            curs.execute(sql, (code_dept,))
            res = curs.fetchall()
        except sqlite3.OperationalError:
            print("DepartementDAO.read: sqlite3.OperationalError")
            return 
        else:
            return Departement(res[0][0], res[0][1], res[0][2])
    
    def read_by_region(self, db_conn, code_region):
        sql = ''' SELECT * 
                  FROM departement
                  WHERE code_region = ?'''
        curs = db_conn.cursor()
        try:
            curs.execute(sql, (code_region,))
            res = curs.fetchall()
        except sqlite3.OperationalError:
            print("DepartementDAO.read_by_region: sqlite3.OperationalError")
            return
        else:
            return res

    def read_all(self, db_conn):
        sql = ''' SELECT * 
                  FROM departement '''
        curs = db_conn.cursor()
        try:
            curs.execute(sql)
            res = curs.fetchall()
        except sqlite3.OperationalError:
            print("DepartementDAO.read_all: sqlite3.OperationalError")
            return 
        else:
            return res

    def update(self, db_conn, code_dept, nom_dept, code_region):
        sql = ''' UPDATE departement
                    SET nom_dept = ?,
                        code_region = ?
                    WHERE id_dept = ?;'''
        values = (nom_dept, code_region, code_dept)
        try:
            db_conn.execute(sql, values)
        except sqlite3.OperationalError:
            print("DepartementDAO.update: sqlite3.OperationalError")
            return False
        else:
            return True
