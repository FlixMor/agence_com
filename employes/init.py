from employesDAO import EmployeDAO
from employes.employe import Employe
#from employe import Employe

employe = Employe("Antoine","Felix","1212","Nettoyeur","JAN")

print(EmployeDAO.add(employe))
#print(message)

#print(EmployeDAO.get_one(1515))