import sqlite3
import time
from Dao import*
class Venda(Dao):
	def __init__(self,cliente = ""):
		Dao.__init__(self)
		self.cliente = cliente
		print("Vendas Criado")

	def Create(self,id,nome_cliente,tipo_ingresso,valor_ingresso):
		data_compra = time.strftime("%d-%m-%y")
		cursor.execute('INSERT INTO Clientes (id,nome_cliente,tipo_ingresso,valor_ingresso, data_compra) VALUES (?,?,?,?,?)', (id,nome_cliente,tipo_ingresso,valor_ingresso, data_compra))
		connection.commit()

	def Read(self,keyword):
		
		sql = 'SELECT * FROM Clientes WHERE Clientes.nome_cliente = ? OR Clientes.tipo_ingresso = ? OR Clientes.valor_ingresso = ?'
		cursor.execute(sql, (keyWord,keyWord,keyWord,))

		dados = cursor.fetchone()
		if dados is None:
			print('Usuario não encontrado em nosso sistema.')
		else:
			
			print("Nome do Cliente: ", dados[1] ," - Tipo do Ingresso: ", dados[2] ," - Valor do Ingresso: ", str(dados[3]) ," - Data da Reserva: ", str(dados[4]))	
			return False

	def ReadAll(self):

		sql = 'SELECT * FROM Clientes '
		cursor.execute(sql)
		
		dados = cursor.fetchall()
		if len(dados) == 0:
			print('Ainda nao temos usuarios cadastrado no sistema.')
		else:
			for info in dados:
				print("Nome do Cliente: ", info[1] ," - Tipo do Ingresso: ", info[2] ," - Valor do Ingresso: ", info[3] ," - Data da Reserva: ", info[4])		

v = Venda()
v.ReadAll()