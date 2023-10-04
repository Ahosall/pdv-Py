# By Feh's

from .utils import genToken

class Sessions:
  def __init__(self, db):
    self._db = db
  
  def create(self, user):
    newToken = genToken(120)
    data = {"user": user, "token": newToken}
    self._db.add(data)
    return data
  
  def destroy(self,):
    return None
  
  def check(self, user, token):
    user = self._db.sessions.byUser(user)
    return False if not user else user['token'] == token