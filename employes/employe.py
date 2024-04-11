class Employe:
    def __init__(self,nom ,prenom, matricule, fonction, departement):
        self.__nom = nom
        self.__prenom = prenom
        self.__matricule = matricule
        self.__fonction = fonction
        self.__departement = departement
        

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, v):
        self.__nom = v

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, v):
        self.__prenom = v

    @property
    def matricule(self):
        return self.__matricule
    @matricule.setter
    def matricule(self, v):
        self.__matricule = v

    @property
    def fonction(self):
        return self.__fonction
    @fonction.setter
    def fonction(self, v):
        self.__fonction = v

    @property
    def departement(self):
        return self.__departement
    @departement.setter
    def departement(self, v):
        self.__departement = v