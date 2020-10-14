from PySide2 import QtWidgets, QtCore
from movie import Movie, get_movies

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()
        self.resize(400, 500)
    
    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_delMovies = QtWidgets.QPushButton("Supprimer le(s) film(s)")
        
        self.layout.addWidget(self.le_movieTitle)
        self.layout.addWidget(self.btn_addMovie)
        self.layout.addWidget(self.lw_movies)
        self.layout.addWidget(self.btn_delMovies)
    
    def setup_connections(self):
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.le_movieTitle.returnPressed.connect(self.add_movie)
        self.btn_delMovies.clicked.connect(self.remove_movie)

    def populate_movies(self):

        movies = get_movies()
        for mov in movies:
            lw_item = QtWidgets.QListWidgetItem(mov.title)
            lw_item.setData(QtCore.Qt.UserRole, mov)
            self.lw_movies.addItem(lw_item)

    def add_movie(self):
        mov_title = self.le_movieTitle.text()
        mov = Movie(mov_title)

        if not mov_title:
            return False

        if mov.add_to_movies():
            self.lw_movies.clear()
            self.populate_movies()
        
        """if mov.add_to_movies():
            lw_item = QtWidgets.QListWidgetItem(mov.title)
            lw_item.setData(QtCore.Qt.UserRole, mov)
            self.lw_movies.addItem(lw_item)"""

        self.le_movieTitle.setText("")

    
    def remove_movie(self):
        for selected_item in self.lw_movies.selectedItems():
            mov = selected_item.data(QtCore.Qt.UserRole)
            mov.remove_from_movies()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = App()
    win.show()
    app.exec_()
