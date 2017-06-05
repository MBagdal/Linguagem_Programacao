import sqlite3
import time

connection = sqlite3.connect('ExemplosPython.db')
cursor = connection.cursor()

class Dao:
	def __init__(self):
		self.CreateTable()
		print("Dao Criado")


	def CreateTable(self):
		cursor.execute('CREATE TABLE IF NOT EXISTS Clientes (id integer, nome_cliente text, tipo_ingresso text, valor_ingresso real, data_compra date)')

