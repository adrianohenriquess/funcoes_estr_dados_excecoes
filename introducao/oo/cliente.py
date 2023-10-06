class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("chamando o metodo getter nome() com @property")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando o metodo setter nome() com @property")
        self.__nome = nome