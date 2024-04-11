import database
#Importation pour le test dans le init.py
#from employe import Employe 

#Importation pour l'exterieur du package
from employes.employe import Employe

class EmployeDAO:
    connexion = database.connexion_db()
    cursor = connexion.cursor()

    @classmethod
    def lister_employes(cls):
        employes = []
        sql = "SELECT * FROM agence"
        try:
            EmployeDAO.cursor.execute(sql)
            users = EmployeDAO.cursor.fetchall()
            message = "Succes"
        except Exception as error:
            message = "Erreur lors de la récupération des utilisateurs"
            users = []
        for user in users:
            id , nom , prenom , matricule , fonction, departement = user
            employes.append({"id":id,"nom":nom,"prenom":prenom,"matricule":matricule, "fonction":fonction, "departement":departement})
        return (employes,message)

    @classmethod
    def add(cls,employe:Employe):
        sql = "INSERT INTO agence(nom,prenom,matricule,fonction,departement) VALUE (%s,%s,%s,%s,%s)"
        params = (employe.nom,employe.prenom,employe.matricule,employe.fonction,employe.departement)
        try:
            EmployeDAO.cursor.execute(sql,params)
            EmployeDAO.connexion.commit()
            message = "success"
            return message
        except Exception as error:
            message = "failure"
            return message
        
    @classmethod
    def get_one(cls, matricule):
        sql = "SELECT * FROM AGENCE  WHERE MATRICULE=%s"
        try:
            EmployeDAO.cursor.execute(sql,(matricule,))
            employe = EmployeDAO.cursor.fetchone()
            message = "success"
            return message, employe
        except Exception as error:
            message = 'failure'
            employe={}
            return message, employe

    @classmethod
    def del_employe(cls, matricule):
        sql = "DELETE FROM agence WHERE matricule =%s"
        try:
            EmployeDAO.get_one(matricule)
            EmployeDAO.cursor.execute(sql, (matricule,))
            EmployeDAO.connexion.commit()
        except ValueError as error:
            print("erreur")
