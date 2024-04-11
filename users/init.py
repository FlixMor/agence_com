import userDAO as UserDAO
import user as User

message, user = UserDAO.UserDAO.get_one('flixu','123456')
print(user)
print(message)