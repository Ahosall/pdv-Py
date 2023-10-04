# By Feh's

from getpass import getpass

from .sessions import Sessions

def loginPage():
  print('#### LOGIN ####')
  user = input("Login: ")
  password = getpass("Senha: ")
  
  return user, password

class Auth:
  def __init__(self, users, sessions):
    self._db = users
    self._sessions = Sessions(sessions)
  
  def auth(self, func):
    def check():
      if self._sessions.check():
        func()
      else:
        print('User is not logged!')
        user, password = loginPage()
        self.login(user, password)

    return check()

  def login(self, user, password):
    self._db
    return False
  
  def logout(self, user):
    return True