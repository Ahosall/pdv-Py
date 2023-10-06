from getpass import getpass

from .db import Database

database = Database('db.json')

users = database.users

def check(login: str, pasw: str):
  user = database.users.byLogin(login)
  if user:
    if user['password'] == pasw:
      return True, user

  return False, None

def login():
  print('==='*8)
  login = input("Login: ")
  passw = getpass("Senha: ")
  print('==='*8)
  
  return check(login, passw)
