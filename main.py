# Imports --------------------------------------------------

import os
import time
import colorama as C

# Colorama Colors-------------------------------------------

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
# Fore: LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX
# Back: LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX

# Variables and Lists --------------------------------------

# Users
with open("user.txt", "r") as txt_users:
  lista_user = txt_users.read().splitlines()

# Passwords
with open("pass.txt", "r") as txt_pass:
  lista_pass = txt_pass.read().splitlines()

# Id's
with open("id.txt", "r") as txt_id:
  lista_id = txt_id.read().splitlines()

# Functions ------------------------------------------------

# Main --------------------------------------------------

time.sleep(0.2)
os.system('clear')
print(C.Fore.LIGHTGREEN_EX + "-" * 30)
print(C.Fore.WHITE + "Bem vindo ao sistema!")
print(C.Fore.WHITE + "Página de Login")
print(C.Fore.LIGHTGREEN_EX + "-" * 30)
#print(f"Lista de usuários: {lista_user}")
#print(f"Lista de senhas: {lista_pass}")
#print(f"Lista de id's: {lista_id}")
while True:
  user = input(C.Fore.WHITE + "Digite seu usuário: \033[34m")
  if user in lista_user:
    id = lista_user.index(user)
    time.sleep(1)
    for i in range(3):
      passw = input(C.Fore.WHITE + "Digite sua senha: \033[34m")
      if passw == lista_pass[id]:
        time.sleep(1)
        print(C.Fore.GREEN + "Login realizado com sucesso.")
      else:
        time.sleep(1)
        print(C.Fore.RED + "Senha incorreta!")
        i += 1
        if i == 3:
          time.sleep(1)
          print(C.Fore.RED + "Você excedeu o número de tentativas!")
          print(C.Fore.RED + "Tente novamente mais tarde.")
          time.sleep(3)
          os.system('clear')
          break
  else:
    time.sleep(1)
    print(C.Fore.RED + "Usuário não encontrado!")
