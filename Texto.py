class Texto:
    def __init__(self, texto: str):
        self.texto = texto

    def devolver_diccionario_frecuencia(self) -> {}:
        diccionario = {}

        aux = self.texto.lower().split(' ')

        for palabra in aux:
            diccionario.setdefault(palabra, 0)

        return diccionario
