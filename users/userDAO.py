#import for init tests
#from user import User

#import for exterieur du package user
from users.user import User
import database

class UserDAO:
    connexion = database.connexion_db()
    cursor = connexion.cursor()

    @classmethod
    def get_one(cls, username, password):
        sql = "SELECT * FROM user WHERE username = %s AND password = %s"
        try:
            UserDAO.cursor.execute(sql, (username,password))
            user = UserDAO.cursor.fetchone()
            if user is None:
                message = "error"
            else:
                message = "success"
        except Exception as error:
            message = "failure"
            user = {}
        return message, user
    
    @classmethod
    def add(cls,user:User):
        sql = "INSERT INTO user(nom_complet,username,password) VALUE (%s,%s,%s)"
        params = (user.nom_complet,user.username,user.password)
        UserDAO.cursor.execute(sql,params)
        UserDAO.connexion.commit()
        message = "success"
        return message