import database
import departements.departement as Departement


class DepartementDAO:
    connexion = database.connexion_db()
    cursor = connexion.cursor()

    @classmethod
    def lister_departements(cls):
        departements = []
        sql = "SELECT * FROM departement"
        try:
            DepartementDAO.cursor.execute(sql)
            departes = DepartementDAO.cursor.fetchall()
            message = "Succes"
        except Exception as error:
            message = "Erreur"
            departes = []
        for dep in departes:
            id , nom , direction , emplacement = dep
            departements.append({"id":id,"nom":nom,"direction":direction,"emplacement":emplacement})
        return (departements,message)
    

    @classmethod
    def add(cls,employe:Departement):
        sql = "INSERT INTO departement(nom,direction,emplacement) VALUE (%s,%s,%s)"
        params = (employe.nom,employe.direction,employe.emplacement)
        try:
            DepartementDAO.cursor.execute(sql,params)
            DepartementDAO.connexion.commit()
            message = "success"
            return message
        except Exception as error:
            message = "failure"
            return message
        
    @classmethod
    def get_one(cls, nom):
        sql = "SELECT * FROM departement WHERE nom=%s"
        try:
            DepartementDAO.cursor.execute(sql,(nom,))
            dep = DepartementDAO.cursor.fetchone()
            message = "Success"
            return message, dep
        except Exception as error:
            message = 'failure'
            dep={}
            return message, dep
        
    @classmethod
    def del_departement(cls, name):
        sql = "DELETE FROM departement WHERE nom= %s"
        try:
            DepartementDAO.cursor.execute(sql, (name,))
            DepartementDAO.connexion.commit()
            
        except ValueError as error:
            print("erreur")