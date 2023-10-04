# By Feh's

import json

def loadDB(path):
  f = open(path, 'w+')
  try:
    d = json.loads(f.read())
    f.close()
    return d
  except:
    newDb = '{"users": [], "products": [], "sessions": []}'
    f.write(newDb)
    d = json.loads(newDb)
    f.close()
    return d

# User Controller Model
class UserController:
  def __init__(self, users: object, db: any):
    self._users = users
    self._db = db
  
  def byId(self, uid: str):
    try:
      return [user for user in self._users if user["id"] == uid][0]
    except:
      return None
    
  def byLogin(self, login: str):
    try:
      return [user for user in self._users if user["login"] == login][0]
    except:
      return None
    
  def add(self, userdata: object):
    try:
      newData = {
        "name": userdata['name'],
        "login": userdata['login'],
        "password": userdata['password'],
        "level": userdata['level']
      }

      if not newData['login'] in [user for user in self._users]:
        self._db._db['users'].append(newData)
        self._db.save()
        return True
      else:
        return False
    except:
      return False
  
  def modify(self, uid: str, userdata: object):
    user = self.byId(uid)
    if not user: raise "User not found!"
    
    edtUser = {**user, **userdata}
    idx = [idx for idx, user in enumerate(self._users) if user['id'] == uid][0]
    self._db._db['users'][idx] = edtUser
    self._db.save()
    return edtUser
  
  def remove(self, uid: str):
    if not self.byId(uid) == None:
      idx = [idx for idx, user in enumerate(self._users) if user['id'] == uid][0]
      del self._db._db['users'][idx]
      self._db.save()
      return True
    else:
      return False

# Product Controller Model
class ProductController:
  def __init__(self, products: object, db: any):
    self._products = products
    self._db = db
    
  def byId(self, uid: str):
    try:
      return [product for product in self._products if product["id"] == uid][0]
    except:
      return None
    
  def add(self, proddata: object):
    try:
      newData = {
        "name": proddata['name'],
        "amount": proddata['amount'],
        "unit": proddata['unit'],
        "price": proddata['price'],
        "description": proddata['description']
      }

      self._db._db['products'].append(newData)
      self._db.save()
      return True
    except:
      return False
  
  def modify(self, uid: str, productdata: object):
    product = self.byId(uid)
    if not product: raise "Product not found!"
    
    edtProduct = {**product, **productdata}
    idx = [idx for idx, product in enumerate(self._products) if product['id'] == uid][0]
    self._db._db['products'][idx] = edtProduct
    self._db.save()
    return edtProduct
  
  def remove(self, uid: str):
    if not self.byId(uid) == None:
      idx = [idx for idx, product in enumerate(self._products) if product['id'] == uid][0]
      del self._db._db['products'][idx]
      self._db.save()
      return True
    else:
      return False
    
# Sessions Controller Model
class SessionsController:
  def __init__(self, sessionss: object, db: any):
    self._sessions = sessionss
    self._db = db
    
  def byUser(self, user: str):
    try:
      return [sessions for sessions in self._sessions if sessions["user"] == user][0]
    except:
      return None
    
  def add(self, sessiondata: object):
    try:
      newData = {
        "user": sessiondata['user'],
        "token": sessiondata['token']
      }

      self._db._db['sessionss'].append(newData)
      self._db.save()
      return True
    except:
      return False
  
  def modify(self, uid: str, sessionsdata: object):
    sessions = self.byId(uid)
    if not sessions: raise "Sessions not found!"
    
    edtSessions = {**sessions, **sessionsdata}
    idx = [idx for idx, sessions in enumerate(self._sessions) if sessions['id'] == uid][0]
    self._db._db['sessionss'][idx] = edtSessions
    self._db.save()
    return edtSessions
  
  def remove(self, uid: str):
    if not self.byId(uid) == None:
      idx = [idx for idx, sessions in enumerate(self._sessions) if sessions['id'] == uid][0]
      del self._db._db['sessionss'][idx]
      self._db.save()
      return True
    else:
      return False

class Database:
  def __init__(self, dbPath):
    self._db = loadDB(dbPath)
    self._path = dbPath

    self.load()

  def save(self):
    f = open(self._path, 'w')
    d = json.dumps(self._db)
    f.write(d)
    f.close()
    return self

  def load(self):
    db = self._db
    self.users = UserController(db['users'], self)
    self.products = ProductController(db['products'], self)
    self.sessions = SessionsController(db['sessions'], self)
    return self
  

Database('teste.json')