import mysql.connector as mysql
def connexion_db():
    connexion = mysql.connect(
        user='root',
        password='',
        host='localhost',
        database='agence'
    )
    return connexion