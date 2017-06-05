import sqlite3
import time
tipo_ingresso = {'Vip': 70, 'Normal': 50,'Estudante': 25};


connection = sqlite3.connect('ExemplosPython.db')
cursor = connection.cursor()

def CreateTable():
	cursor.execute('CREATE TABLE IF NOT EXISTS Clientes (id integer, nome_cliente text, tipo_ingresso text, valor_ingresso real, data_compra date)')

def InsertData(id,nome_cliente, tipo_ingresso,Valor_ingresso, data_compra):

	cursor.execute('INSERT INTO Clientes (id,nome_cliente,tipo_ingresso,valor_ingresso, data_compra) VALUES (?,?,?,?,?)', (id,nome_cliente,tipo_ingresso,Valor_ingresso, data_compra))
	connection.commit()

def CadastrarCliente():
	i = 0
	date = time.strftime("%d-%m-%y")
	while True:
		nome_cliente = input('Digite o nome do cliente: ... s para voltar ao menu principal: ')
		if nome_cliente == 's':
			break
		else:
			tipo_ingresso_cliente = int(input('Digite o Tipo do ingresso: 1 - Vip, 2 - Normal, 3 - Estudante: '))
			if tipo_ingresso_cliente == 1:
				InsertData(i,nome_cliente, "VIP",tipo_ingresso['Vip'],date)
				i = i + 1
			elif tipo_ingresso_cliente == 2:
				InsertData(i,nome_cliente, "Normal",tipo_ingresso['Normal'],date)
				i = i + 1
			elif tipo_ingresso_cliente == 3:
				InsertData(i,nome_cliente, "Estudante",tipo_ingresso['Estudante'],date)
				i = i + 1

def BuscarCliente(keyWord):
	sql = 'SELECT * FROM Clientes WHERE Clientes.nome_cliente = ? OR Clientes.tipo_ingresso = ? OR Clientes.valor_ingresso = ?'
	cursor.execute(sql, (keyWord,keyWord,keyWord,))

	#Tambem pode ser usado desse jeito para verificar se tem dados Gravados no BD
	#data = cursor.fetchall()
	#if len(data) == 0:
	
	dados = cursor.fetchone()
	if dados is None:
		print('Usuario não encontrado em nosso sistema.')
	else:
		
		print("Nome do Cliente: ", dados[1] ," - Tipo do Ingresso: ", dados[2] ," - Valor do Ingresso: ", str(dados[3]) ," - Data da Reserva: ", str(dados[4]))	
			


def DeletarCliente(nome_cliente):
	sql = 'DELETE FROM Clientes WHERE Clientes.nome_cliente = ?'
	cursor.execute(sql,(nome_cliente,))
	connection.commit()
	print('Usuario {} Deletado com sucesso'.format(nome_cliente))

while True:
	CreateTable()
	opc = int(input('Digite 1 - Cadastrar, 2 - Excluir, 3 - Procurar Cliente no sistema: '))
	if opc == 1:
		CadastrarCliente()
	elif opc == 2:
		deletar = input('Digite o nome do cliente para deletar: ')
		DeletarCliente(deletar)	
	elif opc == 3:
		buscar = input('Digite Nome do cliente, ou tipo de Ingresso ou seu Valor: ')
		BuscarCliente(buscar)