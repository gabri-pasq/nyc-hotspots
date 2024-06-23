import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txtDistanza = None
        self.txtStringa = None
        self.ddProvider = None
        self.ddTarget = None
        self.btnCreaGrafo = None
        self.btnAnalisiGrafo = None
        self.btnCalcola = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("NYC- Hotspots", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txtDistanza = ft.TextField(label="Distanza",width=200, hint_text="Insert distance")
        self.btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleCrea)
        row1 = ft.Row([self.txtDistanza,  self.btnCreaGrafo],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.ddProvider = ft.Dropdown(label="Provider",width=200)
        self.btnAnalisiGrafo = ft.ElevatedButton(text="Analisi Grafo", on_click=self._controller.handleAnalisi)
        row2 = ft.Row([self.ddProvider, self.btnAnalisiGrafo],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self._controller.fillProviders()

        self.ddTarget = ft.Dropdown(label="Target",width=200)
        self.btnCalcola = ft.ElevatedButton(text="Calcola", on_click=self._controller.handleCalcola)
        row3 = ft.Row([self.ddTarget, self.btnCalcola],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        self.txtStringa = ft.TextField(label="Stringa",width=200)
        row4 = ft.Row([self.txtStringa],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)

        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
