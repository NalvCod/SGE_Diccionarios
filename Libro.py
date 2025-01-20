class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return (f'El libro con titulo {self.tirulo} escritor por {self.autor}, y con ISBN {self.isbn}'
                f'')

    def __eq__(self, other):
        return self.isbn == other.isbn

    def __hash__(self):
        return hash(self.isbn)