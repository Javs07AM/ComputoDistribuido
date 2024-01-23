import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget

class TareasPendientesGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.tareas = {}

        # Elementos de la interfaz
        self.label = QLabel("Lista de Tareas Pendientes")
        self.lista_tareas = QListWidget()
        self.entry_tarea = QLineEdit()
        self.boton_agregar = QPushButton("Agregar Tarea")
        self.boton_eliminar = QPushButton("Eliminar Tarea")

        # Configurar diseño
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lista_tareas)
        layout.addWidget(self.entry_tarea)
        layout.addWidget(self.boton_agregar)
        layout.addWidget(self.boton_eliminar)

        self.setLayout(layout)

        # Conectar eventos a funciones
        self.boton_agregar.clicked.connect(self.agregar_tarea)
        self.boton_eliminar.clicked.connect(self.eliminar_tarea)

    def agregar_tarea(self):
        descripcion = self.entry_tarea.text()
        tarea_id = len(self.tareas) + 1
        self.tareas[tarea_id] = descripcion
        self.actualizar_lista_tareas()
        self.entry_tarea.clear()

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.currentRow()
        if seleccion >= 0:
            tarea_id = int(self.lista_tareas.item(seleccion).text().split(".")[0])
            if tarea_id in self.tareas:
                tarea_eliminada = self.tareas.pop(tarea_id)
                self.actualizar_lista_tareas()

    def actualizar_lista_tareas(self):
        self.lista_tareas.clear()
        for tarea_id, descripcion in self.tareas.items():
            self.lista_tareas.addItem(f"{tarea_id}. {descripcion}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = TareasPendientesGUI()
    ventana.show()
    sys.exit(app.exec_())
