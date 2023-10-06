# By Feh's

from src.db import Database
from src.auth import login
from src.views import home

database = Database('db.json')

logged = False

def main():
  logged, user = login()

  if logged:
    home.view(user)
  else:
    print('Usuário ou senha inválido!')
    return main()

  return None

if __name__ == "__main__":
  try:
    main()
  except Exception as e:
    print('\nErr:', e)
    exit(1)