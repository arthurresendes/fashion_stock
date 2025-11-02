import sqlite3


def criacao_camisa():
    conexao = sqlite3.connect("fashion.db")
    
    cursor = conexao.cursor()
    
    cursor.execute('''
                CREATE TABLE Camisas(
                    id_camisa INTEGER PRIMARY KEY AUTOINCREMENT,
                    marca VARCHAR(50),
                    tamanho INTEGER,
                    cor VARCHAR(20),
                    genero VARCHAR(20),
                    preco REAL,
                    quantidade INTEGER,
                    promocao BOOL,
                    descricao VARCHAR(100)
                )
    ''')
    
    conexao.commit()
    conexao.close()

def criacao_calca():
    conexao = sqlite3.connect("fashion.db")
    
    cursor = conexao.cursor()
    
    cursor.execute('''
                CREATE TABLE Calcas(
                    id_calcas INTEGER PRIMARY KEY AUTOINCREMENT,
                    marca VARCHAR(50),
                    tamanho INTEGER,
                    cor VARCHAR(20),
                    genero VARCHAR(20),
                    preco REAL,
                    quantidade INTEGER,
                    promocao BOOL,
                    descricao VARCHAR(100)
                )
    ''')
    
    conexao.commit()
    conexao.close()


def criacao_calca():
    conexao = sqlite3.connect("fashion.db")
    
    cursor = conexao.cursor()
    
    cursor.execute('''
                CREATE TABLE Calcas(
                    id_calcas INTEGER PRIMARY KEY AUTOINCREMENT,
                    marca VARCHAR(50),
                    tamanho INTEGER,
                    cor VARCHAR(20),
                    genero VARCHAR(20),
                    preco REAL,
                    quantidade INTEGER,
                    promocao BOOL,
                    descricao VARCHAR(100)
                )
    ''')
    
    conexao.commit()
    conexao.close()

def criacao_informacoes_vendas():
    conexao = sqlite3.connect("fashion.db")
    
    cursor = conexao.cursor()
    
    cursor.execute('''
                CREATE TABLE Informacoes_vendas(
                    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
                    marca VARCHAR(50),
                    tamanho INTEGER,
                    cor VARCHAR(20),
                    preco REAL,
                    quantidade INTEGER,
                    preco_total REAL,
                    data_venda DATETIME
                )
    ''')
    
    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criacao_camisa()
    criacao_calca()
    criacao_informacoes_vendas()