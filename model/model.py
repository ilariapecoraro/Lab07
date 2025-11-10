from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()
        self._musei = []
        self._epoche = []
        self._artefatti = []

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):

        if museo == "Nessun filtro" and epoca == "Nessun filtro":
            self._artefatti = ArtefattoDAO.read_all_artefatti()
        elif museo == "Nessun filtro":
            self._artefatti = ArtefattoDAO.read_artefatti_for_epoca(epoca)
        elif epoca == "Nessun filtro":
            self._artefatti = ArtefattoDAO.read_artefatti_for_museums(museo)
        else:
            self._artefatti = ArtefattoDAO.read_artefatti_for_epoca_and_museum(museo,epoca)
        return self._artefatti

        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO

    def get_epoche(self):
        if len(self._epoche) == 0:
            self._epoche = ArtefattoDAO.read_all_epoche()
            self._epoche.append("Nessun filtro")
        else:
            print("Just read from database using SQL query")
        return self._epoche

        """Restituisce la lista di tutte le epoche."""
        # TODO

    # --- MUSEI ---
    def get_musei(self):
        if len(self._musei) == 0:
            self._musei = MuseoDAO.read_all_museums()
            self._musei.append("Nessun filtro")
        else:
            print("just read from database using SQL query")
        return self._musei
        """ Restituisce la lista di tutti i musei."""
        # TODO

