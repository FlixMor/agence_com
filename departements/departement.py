class Departement:
    def __init__(self,nom ,direction , emplacement):
        self.__nom = nom
        self.__direction = direction
        self.__emplacement = emplacement
        
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, v):
        self.__nom = v

    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self, v):
        self.__direction = v

    @property
    def emplacement(self):
        return self.__emplacement
    @emplacement.setter
    def emplacement(self, v):
        self.__matricule = v
