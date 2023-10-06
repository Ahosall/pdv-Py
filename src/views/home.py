# By Feh's
from time import sleep as wait

from src.utils import brand
from . import pdv, estoque, gerencia

gerenciaMenu = [
  '  Gerenciamento:              ',
  '    [10]: Produtos            ',
  '    [11]: Usuários            ',
  '    [12]: Vendas              ',
  '                              ',
  '    [00]: Sair                ',
  '                              ',
]

def view(user: object):
  brand()
  v = [
    '=== Início                   ',
    '  Telas:                      ',
    '    [01]: PDV                 ',
    '    [02]: Estoque             ', 
    '                              ',
  ]

  if user['level'] == 99: v = [*v, *gerenciaMenu]
  
  print('\n'.join(v))
  opt = input('  ::> ')

  if not opt.isdigit():
    print('Opção incorreta!')
    wait(3)
    return view(user)
  
  if int(opt) == 0:
    brand()
    print('\nAté mais!')
    exit(0)
  elif int(opt) == 1:
    return pdv.view()
  elif int(opt) == 2:
    return estoque.view()
  elif int(opt) == 10:
    return gerencia.products.view()
  elif int(opt) == 11:
    return gerencia.users.view()
  elif int(opt) == 12:
    return gerencia.vendas.view()
  else:
    print('Opção incorreta! Aguarde 3 segundos...')
    wait(3)
    return view(user)