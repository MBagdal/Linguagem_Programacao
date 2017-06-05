pessoa = []
print('Seja Bem Vindo ao sistema de cadastro do Bagdal')

def Cadastrar():
	while True:
		nome = input('Digite Um nome para cadastrar: ... ou s para sair: ')
		if nome == 's':
			break
		elif nome != 's':
			pessoa.append(nome)

def Excluir():
	nome_exluir = input('Digite um nome para excluir: ')
	if len(pessoa) == 0:
		print('Por favor Cadastre um usuario')
	elif nome_exluir in pessoa:
		del pessoa[pessoa.index(nome_exluir)]
		print('Usuario ' + nome_exluir + ' foi excluido com sucesso')
	else:
		print('Usuario nao encontrado')
			
def ProcurarUsuario():
	print('Usuarios encontrado no sistema: ')
	for nome in pessoa:
		print(nome)

while True:
	opc = int(input('Digite 1 - Cadastrar, 2 - Excluir, 3 - Procurar Usuadios no sistema: '))
	if opc == 1:
		Cadastrar()
	elif opc == 2: 
		Excluir()
	elif opc == 3:
		ProcurarUsuario()

