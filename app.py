from flask import Flask, render_template, url_for, request, session, redirect
from employes.employesDAO import  EmployeDAO
from employes.employe import Employe
from departements.departementDAO import DepartementDAO
from departements.departement import Departement
from users.userDAO import UserDAO
from users.user import User

app = Flask(__name__)
app.secret_key = "clesecrete"

# Routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/employes')
def employes():
    if 'username' not in session:
        return redirect(url_for('login'))
    (liste_employes,message) = EmployeDAO.lister_employes()
    return render_template('employes.html', liste_employes=liste_employes)

@app.route('/departement')
def departements():
    if 'username' not in session:
        return redirect(url_for('login'))
    (liste_departements, message) = DepartementDAO.lister_departements()
    return render_template('departements.html', liste_departements=liste_departements)

@app.route('/add-employe', methods=['POST','GET'])
def add_employe():
    if 'username' not in session:
        return redirect(url_for('login'))
    req = request.form
    message=None
    if request.method == 'POST':
        nom = req["nom"]
        prenom = req["prenom"]
        matricule = req["matricule"]
        fonction = req["fonction"]
        departement = req["departement"]
        if nom=="" or prenom=="" or matricule=="" or fonction=="" or  departement=="":
            message = "error"
        else:
            employe = Employe(nom,prenom,matricule,fonction,departement)
            #print(employe.nom, employe.prenom, employe.matricule)
            message = EmployeDAO.add(employe)
    return render_template('add_employe.html', message=message)


@app.route('/add-departement', methods=['POST','GET'])
def add_departement():
    if 'username' not in session:
        return redirect(url_for('login'))
    req = request.form
    print(req)
    message=None
    print("Methode HTTP utilisee", request.method)
    if request.method == 'POST':
        nom = req["nom"]
        direction = req["direction"]
        emplacement = req["emplacement"]
        departement = Departement(nom,direction,emplacement)
        print(departement.nom, departement.direction, departement.emplacement)
        message = DepartementDAO.add(departement)
    return render_template('add_departement.html', message=message)

@app.route('/del-employe', methods=['POST','GET'])
def del_employe():
    if 'username' not in session:
        return redirect(url_for('login'))
    req = request.form
    if request.method == 'POST':
        matricule = req['matricule']
        EmployeDAO.del_employe(matricule)
    return render_template('del_employe.html')
    
@app.route('/del-departement', methods=['POST','GET'])
def del_departement():
    if session['username'] != 'admin':
        return redirect(url_for('login'))
    req = request.form
    if request.method == 'POST':
        nom = req['nom']
        DepartementDAO.del_departement(nom)
    return render_template('del_departement.html')

@app.route('/login', methods=['POST','GET'])
def login():
    message = None
    user = None
    req = request.form
    if request.method == 'POST':
        username = req['username']
        password = req['password']
        if username == '' or password == '':
            message = 'invalide'
        else:
            message, user = UserDAO.get_one(username,password)
            if message == 'success' and user != None:
                session['username'] = user[2] #on met la variable username dans la session
                session['nom_complet'] = user[1] #on met la variable nom_complet dans la session
                return redirect(url_for('home'))          
    return render_template('login.html', message=message, user=user)

@app.route('/register',methods=['POST','GET'])
def register():
    message = None
    req = request.form
    if request.method == 'POST':
        nom_complet = req['nom_complet']
        username = req['username']
        password = req['password']
        if nom_complet == '' or username == '' or password == '':
            message = 'invalide'
        else:
            try:
                user = User(nom_complet,username,password)
                message = UserDAO.add(user)
            except Exception as error:
                message = 'failure'

    return render_template('register.html', message=message)

@app.route('/logout',methods=['POST','GET'])
def logout():
    session.clear()
    return redirect(url_for('home'))
