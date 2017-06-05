import sqlite3
import time

conexao = sqlite3.connection('ExemplosPython.db')
cursor. = conexao.cursor()

class Cadastro:

	def __init__(self,nome_cliente,tipo_ingresso_cliente,preco_ingresso):

		self._nome_cliente   = nome_cliente
		self._tipo_ingresso  = tipo_ingresso_cliente
		self._preco_ingresso = nome_cliente
		

	def CreateTable(self):

		cursor.execute('CREATE TABLE IF NOT EXISTS Clientes (id integer, nome_cliente text, tipo_ingresso text, valor_ingresso real, data_compra date)')

	def Create(self):

		cursor.execute('INSERT INTO Clientes (id,nome_cliente,tipo_ingresso,valor_ingresso, data_compra) VALUES (?,?,?,?,?)', (id,nome_cliente,tipo_ingresso,Valor_ingresso, data_compra))
		connection.commit()

	def Read(self):

		sql = 'SELECT * FROM Clientes WHERE Clientes.nome_cliente = ? OR Clientes.tipo_ingresso = ? OR Clientes.valor_ingresso = ?'
		cursor.execute(sql, (keyWord,keyWord,keyWord,))
		
		dados = cursor.fetchone()
		if dados is None:
			print('Usuario não encontrado em nosso sistema.')
		else:
			
			print("Nome do Cliente: ", dados[1] ," - Tipo do Ingresso: ", dados[2] ," - Valor do Ingresso: ", dados[3] ," - Data da Reserva: ", dados[4])

	def ReadAll(self):

		sql = 'SELECT * FROM Clientes '
		cursor.execute(sql)
		
		dados = cursor.fetchall()
		if len(dados) == 0:
			print('Usuario não encontrado em nosso sistema.')
		else:
			
			print("Nome do Cliente: ", dados[1] ," - Tipo do Ingresso: ", dados[2] ," - Valor do Ingresso: ", dados[3] ," - Data da Reserva: ", dados[4])

	def Update():

	def Delete():

		sql = 'DELETE FROM Clientes WHERE Clientes.nome_cliente = ?'
		cursor.execute(sql,(nome_cliente,))
		connection.commit()
		print('Usuario {} Deletado com sucesso'.format(nome_cliente))


