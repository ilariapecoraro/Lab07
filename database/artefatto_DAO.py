from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    @staticmethod
    def read_all_artefatti():
        artefatti = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
            FROM artefatto"""
        cursor.execute(query)
        for row in cursor:
            artefatto = Artefatto(row["id"], row["nome"], row["tipologia"],
                                  row["epoca"], row["id_museo"])
            artefatti.append(artefatto)
        cursor.close()
        cnx.close()
        return artefatti

    @staticmethod
    def read_artefatti_for_museums(id_museo):
        artefatti = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT a.*
         FROM artefatto a, museo m
         WHERE m.nome = %s 
         AND a.id_museo = m.id"""
            cursor.execute(query, (id_museo,))
            for row in cursor:
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"],
                                      row["epoca"], row["id_museo"])
                artefatti.append(artefatto)
            cursor.close()
            cnx.close()
            return artefatti

    @staticmethod
    def read_artefatti_for_epoca(epoca):
        artefatti = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
            FROM artefatto
            WHERE artefatto.epoca = %s"""
            cursor.execute(query, (epoca,))
            for row in cursor:
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"],
                                      row["epoca"], row["id_museo"])
                artefatti.append(artefatto)
        cursor.close()
        cnx.close()
        return artefatti

    @staticmethod
    def read_all_epoche():
        epoche = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT epoca
            FROM artefatto
            GROUP BY epoca
            ORDER BY epoca ASC"""
            cursor.execute(query)
            for row in cursor:
                epoche.append(row["epoca"])
            cursor.close()
            cnx.close()
            return epoche

    @staticmethod
    def read_artefatti_for_epoca_and_museum(museo,epoca):
        artefatti = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query =  """SELECT a.*
        FROM artefatto a
        JOIN museo m ON a.id_museo = m.id
        WHERE m.nome = %s AND a.epoca = %s"""
            cursor.execute(query, (museo,epoca))
            for row in cursor:
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"],
                                      row["epoca"], row["id_museo"])
                artefatti.append(artefatto)
            cursor.close()
            cnx.close()
            return artefatti
    # TODO