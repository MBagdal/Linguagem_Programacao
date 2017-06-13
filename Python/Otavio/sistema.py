Skip to content
This repository
Search
Pull requests
Issues
Marketplace
Gist
 @MBagdal
 Sign out
 Unwatch 2
  Star 0
  Fork 1 MBagdal/AulasPython
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Settings Insights 
Branch: master Find file Copy pathAulasPython/Otavio/sistema.py
8fa0382  9 days ago
@oNascimento oNascimento Meus Arquivos_BD
1 contributor
RawBlameHistory     
59 lines (46 sloc)  1.3 KB
import sqlite3
import time

conexao = sqlite3.connect("cliente.db")
cursor = conexao.cursor()		

class Cliente:
	def __init__(self,nome,idade,cpf,email,fone,cidade,uf):
		self._nome = nome
		self._idade = idade
		self._cpf = cpf
		self._email = email
		self._fone = fone
		self._cidade = cidade
		self._uf = uf
		
		
	def Cria_Tabela(self):
		cursor.execute("""
			CREATE TABLE if not exists clientes(
				id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
				nome TEXT NOT NULL,
				idade INTEGER,
				cpf     VARCHAR(11) NOT NULL,
				email TEXT NOT NULL,
				fone TEXT,
				cidade TEXT,
				uf VARCHAR(2) NOT NULL,
				criado_em DATE NOT NULL);
			""")

		print('Tabela criada com sucesso.')
	
	def Cadastrar_Cliente(self):
		data = time.strftime("%d,%m,%y")
		
		cursor.execute("""
			INSERT INTO clientes (nome,idade,cpf,email,fone,cidade,uf,criado_em) 
			VALUES (?,?,?,?,?,?,?,?);
			""",(self._nome,self._idade,self._cpf,self._email,self._fone,self._cidade,self._uf,data))
		
		conexao.commit()
		print("Dados Gravados com sucesso");
		
	def Mostrar_Cliente(self):
		cursor.execute("""
			SELECT * FROM clientes;
			""")
		
		for linha in cursor.fetchall():
			print(linha)
			
		conexao.close()
			
		
c = Cliente('Otavio',21,1231,'ksdafh',14123123,'Medianeira','PR')
c.Cria_Tabela()
c.Cadastrar_Cliente()
c.Mostrar_Cliente()
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help