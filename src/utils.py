# By Feh's

import random

def genToken(size):
  chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890@#$_."
  tkn = ""
  for x in range(0, size):
    tkn += random.choice(chars)
  tkn += f"-{int(size/2)}"
  return tkn
