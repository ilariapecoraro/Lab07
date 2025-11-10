import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN

    def handler_popola_musei(self):
        musei = self._model.get_musei()
        for museo in musei:
            self._view._dd_museo.options.append(ft.dropdown.Option(museo))
        self._view.update()

    def handler_popola_epoca(self):
        epoche = self._model.get_epoche()
        for epoca in epoche:
            self._view._dd_epoca.options.append(ft.dropdown.Option(epoca))
        self._view.update()
    # TODO

    # CALLBACKS DROPDOWN

    def handler_save_museo(self,e):
       if self._view._dd_museo.value is None:
           self._view.show_alert("Error select museo first")
       else:
           self.museo_selezionato = self._view._dd_museo.value

    def handler_save_epoca(self,e):
        if self._view._dd_epoca.value is None:
            self._view.show_alert("Error select epoca first")
        else:
            self.epoca_selezionata = self._view._dd_epoca.value


    # TODO

    # AZIONE: MOSTRA ARTEFATTI

    def handler_show_artefatti(self,e):
        if self.museo_selezionato is None or self.epoca_selezionata is None:
            self._view.show_alert("Seleziona prima un museo e un'epoca!")
            return
        self._view._lst_artefatti.controls.clear()
        try:
            artefatti = self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)
            if not artefatti:
                self._view._lst_artefatti.controls.append(ft.Text("Nessun artefatto trovato", color="red"))
            else:
                for artefatto in artefatti:
                    artefatto_widget = ft.Text(f"{artefatto.id} | {artefatto.nome}-{artefatto.tipologia}-{artefatto.epoca}")
                    self._view._lst_artefatti.controls.append(artefatto_widget)
        except Exception as e:
            self._view.show_alert(f"Errore: {str(e)}")


        self._view.update()

    # TODO
