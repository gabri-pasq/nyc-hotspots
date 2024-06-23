import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillProviders(self):
        providers = self._model.getPronviders()
        for p in providers:
            self._view.ddProvider.options.append(ft.dropdown.Option(text=p, key=p))
        self._view.update_page()
    def handleCrea(self, e):
        lista = self._model.creaGrafo(self._view.ddProvider.value, self._view.txtDistanza.value)
        self._view.txt_result.controls.append(ft.Text(self._model.grafoDetatails()))
        for l in lista:
            self._view.txt_result.controls.append(ft.Text(f"{l[0]} - nodi: {l[1]}"))
        self._view.update_page()
    def handleAnalisi(self, e):
        pass

    def handleCalcola(self, e):
        pass