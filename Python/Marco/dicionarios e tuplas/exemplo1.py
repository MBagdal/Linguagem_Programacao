tipo_ingresso = {'Vip': 70, 'Normal': 50,'Estudante': 25};
cliente       = {}

def CadastrarCliente():
	while True:
		nome_cliente = input('Digite o nome do cliente: ... s para voltar ao menu principal: ')
		if nome_cliente == 's':
			break
		else:
			tipo_ingresso_cliente = int(input('Digite o Tipo do ingresso: 1 - Vip, 2 - Normal, 3 - Estudante: '))
			if tipo_ingresso_cliente == 1:
				cliente[nome_cliente] = tipo_ingresso['Vip']
			elif tipo_ingresso_cliente == 2:
				cliente[nome_cliente] = tipo_ingresso['Normal']
			elif tipo_ingresso_cliente == 3:
				cliente[nome_cliente] = tipo_ingresso['Estudante']

def ListarClientes():
	for cli in cliente:
		
		print("\n| Nome do Cliente: ", cli , "- Cliente: ", list(tipo_ingresso.keys())[list(tipo_ingresso.values()).index(cliente[cli])],"- Total: " , str(cliente[cli]), "\n")

while True:
	opc = int(input('Digite 1 - Cadastrar, 2 - Excluir, 3 - Procurar Cliente no sistema: '))
	if opc == 1:
		CadastrarCliente()
	elif opc == 2: 
		Excluir()
	elif opc == 3:
		ListarClientes()