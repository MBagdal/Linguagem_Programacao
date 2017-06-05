import sqlite3
import time

class Cliente:

	def __init__(self, nome_cliente = "", tipo_ingresso = "", valor_ingresso = ""):
		self.__nome_cliente   = nome_cliente
		self.__tipo_ingresso  = tipo_ingresso
		self.__valor_ingresso = valor_ingresso
		print("Criou")


	@property
	def nome_cliente(self):
		return self.__nome_cliente

	@nome_cliente.setter
	def nome_cliente(self,nome_cliente):
		self.__nome_cliente = nome_cliente

	@property
	def tipo_ingresso(self):
		return self.__tipo_ingresso

	@tipo_ingresso.setter
	def tipo_ingresso(self,tipo_ingresso):
		self.__tipo_ingresso = tipo_ingresso

	@property
	def valor_ingresso(self):
		return self.__valor_ingresso

	@valor_ingresso.setter
	def valor_ingresso(self,valor_ingresso):
		self.__valor_ingresso = valor_ingresso

