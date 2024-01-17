import os
import time
import colorama as C
import fileinput
import shutil
from datetime import datetime

# Backup 

time.sleep(0.2)
os.system('cls')

def realizar_backup():
    os.chdir("backup-dados.txt")
    backups = os.listdir()
    if len(backups) >= 10:
        print(C.Fore.LIGHTGREEN_EX + "-" * 30)
        print(C.Fore.LIGHTRED_EX + 'O limite de backups foi atingido.')
        print(C.Fore.LIGHTRED_EX + "Para continuar, você precisa excluir o backup mais antigo:", backups[0])
        resp_backup = input(C.Fore.LIGHTRED_EX + 'Deseja excluí-lo agora [s/n]? ' + C.Fore.CYAN)
        if resp_backup == "s":
            resp_backup = input(C.Fore.LIGHTRED_EX + f"Tem certeza que deseja excluir o backup {backups[0]} [s/n]? " + C.Fore.CYAN)
            print(C.Fore.LIGHTGREEN_EX + "-" * 30)
            if resp_backup == "s":
                print(C.Fore.GREEN + "O backup está sendo excluído e logo um mais recente será gerado.")
                time.sleep(2)
                os.remove(backups[0])
                print(C.Fore.GREEN + 'O backup foi excluído com sucesso.')
                print(C.Fore.LIGHTGREEN_EX + "-" * 30)
                time.sleep(3)
        else:
            
            time.sleep(2)
            print(C.Fore.LIGHTGREEN_EX + "-" * 30)
            print(C.Fore.RED + 'O backup não foi excluído.')
            print(C.Fore.RED + "Por motivos de segurança o programa não poderá continuar.")
            input(C.Fore.RED + "Pressione enter para sair.")
            print(C.Fore.LIGHTGREEN_EX + "-" * 30)
            time.sleep(2)
            exit()
    data_hora_atual = datetime.now().strftime("%d-%m-%y__%H-%M-%S")
    nome_backup = f"backup_{data_hora_atual}.txt"
    shutil.copyfile("../dados.txt", nome_backup)
    print(C.Fore.GREEN + "Backup realizado com sucesso!")
    os.chdir("..")

realizar_backup()

# Variables ---------------------------------------------------

logged = False

# Lists --------------------------------------------------------

with open("dados.txt", "r") as txt_dados:
    linhas = txt_dados.read().splitlines()


lista_user = []
lista_pass = []
lista_id = []
lista_admin = []

for linha in linhas:
    dados = linha.split(',')
    lista_user.append(dados[0])
    lista_pass.append(dados[1])
    lista_id.append(dados[2])
    lista_admin.append(dados[3])

# Functions -------------------------------------------------------

# Main ------------------------------------------------------------

time.sleep(0.2)
os.system('cls')
print(C.Fore.LIGHTGREEN_EX + "-" * 30)
print(C.Fore.WHITE + "Página de Login")
print(C.Fore.LIGHTGREEN_EX + "-" * 30)

if logged == False:
    while logged != True:
        tentativas = 0
        user = input(C.Fore.WHITE + "Digite seu usuário: \033[34m")
        user = user.lower()
        if user in lista_user:
            id = lista_user.index(user)
            time.sleep(1)
            while tentativas != 3 and logged == False:
                passw = input(C.Fore.WHITE + "Digite sua senha: \033[34m")
                if passw == lista_pass[id]:
                    time.sleep(1)
                    print(C.Fore.GREEN + "Login realizado com sucesso.")
                    logged = True
                else:
                    time.sleep(1)
                    print(C.Fore.RED + "Senha incorreta!")
                    tentativas += 1
                    if tentativas == 3:
                        time.sleep(1)
                        print(C.Fore.RED + "Você excedeu o número de tentativas!")
                        print(C.Fore.RED + "Tente novamente mais tarde.")
                        time.sleep(3)
                        os.system('cls')
                        break
        else:
            time.sleep(1)
            print(C.Fore.RED + "Usuário não encontrado!")

if logged == True:
    while logged == True:
        time.sleep(1)
        os.system('cls')
        print(C.Fore.LIGHTGREEN_EX + "-" * 30)
        print(C.Fore.WHITE + "Bem vindo ao sistema!")
        if user in lista_user and lista_admin[lista_user.index(user)] == 'y':
            print(C.Fore.WHITE + "Você está logado como " + C.Fore.LIGHTRED_EX +
                "administrador.")
        print(C.Fore.LIGHTGREEN_EX + "-" * 30)
        print(C.Fore.WHITE + "Escolha uma opção:")
        print(C.Fore.WHITE + "1 - Listar usuários")
        if user in lista_user and lista_admin[lista_user.index(user)] == 'y':
            print(C.Fore.WHITE + "2 - Cadastrar usuário")
            print(C.Fore.WHITE + "3 - Excluir usuário")
            print(C.Fore.WHITE + "4 - Alterar senha")
            print(C.Fore.WHITE + "5 - Alterar senha")
        print(C.Fore.WHITE + "0 - Sair")
        print(C.Fore.LIGHTGREEN_EX + "-" * 30)
        opcao = input(C.Fore.WHITE + "Digite a opção desejada: \033[34m")
        try:
            opcao = int(opcao)
        except:
            time.sleep(1)
            print(C.Fore.RED + "Opção inválida!")
            time.sleep(1)
            os.system('cls')
            continue
        print(C.Fore.LIGHTGREEN_EX + "-" * 30)
        if opcao == 1:
            print(C.Fore.WHITE + "Lista de usuários:")
            for i in range(len(lista_user)):
                print(C.Fore.MAGENTA + f"{i+1} - {lista_user[i]}")
            print(C.Fore.LIGHTGREEN_EX + "-" * 30)
            opcao = input(
                C.Fore.WHITE +
                "Deseja ver mais informações de algum usuário? (s/n): \033[34m")
            if opcao == "s":
                opcao = input(C.Fore.WHITE + "Digite o nome ou número do usuário: \033[34m")
                print(C.Fore.LIGHTGREEN_EX + "-" * 30)
                if opcao.isdigit():
                    try:
                        opcao = int(opcao)
                    except:
                        print(
                            C.Fore.RED +
                            "Falha na conversão da variável opcao para int. O valor digitado pode não ser um número inteiro. Value=",
                            opcao, " | Type=", type(opcao))
                        continue
                    if opcao > len(lista_user) or opcao < 1:
                        print(C.Fore.RED +
                            "Opção menor que 1 ou maior que o número de usuários.")
                        continue
                    else:
                        print(C.Fore.WHITE +
                            f"Informações do usuário {lista_user[opcao-1]}:")
                        print(C.Fore.WHITE + f"Nome:", C.Fore.MAGENTA,
                            lista_user[opcao - 1])
                        print(C.Fore.WHITE + f"ID: {lista_id[opcao-1]}")
                        if lista_admin[lista_user.index(lista_user[opcao - 1])] == 'y':
                            print(C.Fore.WHITE + f"Administrador:\033[1;33m Sim")
                        else:
                            print(C.Fore.WHITE + f"Administrador:\033[1;33m Não")
                        print(C.Fore.LIGHTGREEN_EX + "-" * 30)
                        opcao2 = input(
                            C.Fore.WHITE +
                            "Pressione enter para voltar...")
                        os.system('cls')
                else:
                    if opcao in lista_user:
                        print(C.Fore.WHITE + f"Informações do usuário", C.Fore.MAGENTA,
                            opcao, ":")
                        print(C.Fore.WHITE + f"Nome:", C.Fore.MAGENTA, opcao)
                        print(C.Fore.WHITE + f"ID: {lista_id[lista_user.index(opcao)]}")
                        if lista_admin[lista_user.index(lista_user[opcao - 1])] == 'y':
                            print(C.Fore.WHITE + f"Administrador:\033[1;33m Sim")
                        else:
                            print(C.Fore.WHITE + f"Administrador:\033[1;33m Não")
                    else:
                        print(C.Fore.RED + "Usuário não encontrado!")
                    time.sleep(1)
                    print(C.Fore.LIGHTGREEN_EX + "-" * 30)
                    input(C.Fore.WHITE + 'Pressione enter para voltar...')
                    os.system('cls')
        elif opcao == 2:
            if user in lista_user and lista_admin[lista_user.index(user)] == 'y':
                print(C.Fore.WHITE + "Cadastrar usuário:")
                new_user = input(C.Fore.WHITE + "Digite o nome do usuário: \033[34m")
                if any(new_user.lower() == item.lower() for item in lista_user):
                    time.sleep(1)
                    print(C.Fore.RED + "Usuário já cadastrado!")
                    time.sleep(1)
                else:
                    senha = input(C.Fore.WHITE + 'Digite a senha do usuário: \033[34m')
                    print('O último ID cadastrado no sistema é: ' + C.Fore.LIGHTRED_EX, len(lista_user))
                    id_usuario = input(C.Fore.WHITE + 'Digite o ID do usuário: \033[34m')
                    is_admin = input(C.Fore.WHITE + 'O usuário é administrador? (s/n): \033[34m')
                    if is_admin == "s":
                        is_admin = "y"
                    else:
                        is_admin = "n"
                    dados_string = f"{new_user.lower()},{senha},{id_usuario},{is_admin.lower()}"
                    
                    lista_user.append(new_user.lower())
                    lista_pass.append(senha)
                    lista_id.append(id_usuario)
                    lista_admin.append(is_admin.lower())
                    with open("dados.txt", "a") as txt_dados:
                        txt_dados.write("\n" + dados_string)
                    time.sleep(1)
                    print(C.Fore.LIGHTGREEN_EX + "-" * 30)
                    print(C.Fore.GREEN + "Usuário cadastrado com sucesso!")
                    print(C.Fore.WHITE + "Voltando para o menu...")
                    print(C.Fore.LIGHTGREEN_EX + "-" * 30)
                    time.sleep(4)
        elif opcao == 3:
            if user in lista_user and lista_admin[lista_user.index(user)] == 'y':
                print(C.Fore.WHITE + "Excluir usuário:")
                opcao = input(C.Fore.WHITE + "Digite o nome ou ID do usuário: \033[34m")
                print(C.Fore.LIGHTGREEN_EX + "-" * 30)
                if opcao.isdigit():
                    try:
                        opcao = int(opcao)
                    except:
                        print(
                            C.Fore.RED + "Falha na conversão da variável opcao para int. O valor digitado pode não ser um número inteiro. Value=", opcao, " | Type=", type(opcao))
                        time.sleep(3)
                        os.system('cls')
                        continue
                    if opcao > len(lista_user) or opcao < 1:
                        print(C.Fore.RED +
                            "Opção menor que 1 ou maior que o número de usuários.")
                        time.sleep(3)
                        os.system('cls')
                        continue
                    else:
                        print(C.Fore.WHITE +
                            f"Informações do usuário {lista_user[opcao-1]}:")
                        print(C.Fore.WHITE + f"Nome:", C.Fore.MAGENTA,
                            lista_user[opcao - 1])
                        print(C.Fore.WHITE + f"ID: {lista_id[opcao-1]}")
                        if lista_admin[lista_user.index(lista_user[opcao - 1])] == 'y':
                            print(C.Fore.WHITE + f"Administrador:\033[1;33m Sim")
                        else:
                            print(C.Fore.WHITE + f"Administrador:\033[1;33m Não")
                        print(C.Fore.LIGHTGREEN_EX + "-" * 30)
                        print(C.Fore.LIGHTGREEN_EX + "-" * 30)
                        resp = input("Tem certeza que deseja excluir esse usuário? (s/n): ")
                        if resp.lower() == "s":
                            if str(opcao) in lista_id:
                                lista_user.pop(opcao-1)
                                lista_pass.pop(opcao-1)
                                lista_id.pop(opcao-1)
                                lista_admin.pop(opcao-1)
                                with open("dados.txt", "w") as txt_dados:
                                    for i in range(len(lista_user)):
                                        if i != len(lista_user)-1:
                                            txt_dados.write(f"{lista_user[i]},{lista_pass[i]},{lista_id[i]},{lista_admin[i]}\n")
                                        else:
                                            txt_dados.write(f"{lista_user[i]},{lista_pass[i]},{lista_id[i]},{lista_admin[i]}")  
                                time.sleep(1)
                                print(C.Fore.LIGHTGREEN_EX + "-" * 30)
                                print(C.Fore.GREEN + "Usuário excluído com sucesso!")
                                print(C.Fore.WHITE + "Voltando para o menu...")
                                print(C.Fore.LIGHTGREEN_EX + "-" * 30)
                                time.sleep(4)
                            else:
                                print(C.Fore.RED + "Usuário não encontrado!")
                                time.sleep(1)
                        os.system('cls')
