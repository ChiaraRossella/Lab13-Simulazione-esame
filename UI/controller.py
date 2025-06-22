import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleCreaGrafo(self,e):
        self._view.txt_result.controls.clear()
        if self._view._ddAnno.value is None:
            self._view.txt_result.controls.append(ft.Text("Selezionare un anno dalla tendina"))
            return
        anno=int(self._view._ddAnno.value)
        self._model.createGraph(anno)
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato:"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {self._model.get_num_nodes()}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {self._model.get_num_archi()}"))
        pilota, score = self._model.getBestPilota()
        self._view.txt_result.controls.append(ft.Text(f"Best Driver: {pilota}, with score {score}"))
        self._view.update_page()


    def handleCerca(self, e):
        self._view.txt_result.controls.clear()
        if self._view._ddAnno.value is None:
            self._view.txt_result.controls.append(ft.Text("Selezionare un anno dalla tendina"))
            return
        anno = int(self._view._ddAnno.value)


    def fillDDYear(self):
        years=self._model.get_years()
        listYears= [ ft.dropdown.Option(y) for y in years]
        self._view._ddAnno.options=listYears