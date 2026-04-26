import sqlite3

def conexao_inicial():
    conexao = sqlite3.connect("LoginUser.db")
    cursor = conexao.cursor()
    return conexao,cursor

def fechamento(conexao):
    conexao.commit()
    conexao.close()

def criacao_table_user():
    conexao,cursor = conexao_inicial()
    cursor.execute('''
                CREATE TABLE Usuario(
                    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(50),
                    senha VARCHAR(30)
                )
    ''')
    fechamento(conexao)

def criacao_table_produto():
    conexao,cursor = conexao_inicial()
    cursor.execute('''
                CREATE TABLE Produto(
                    id_prod INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo VARCHAR(20),
                    marca VARCHAR(50),
                    tamanho INTEGER,
                    cor VARCHAR(20),
                    genero VARCHAR(20),
                    preco_unitario FLOAT,
                    quantidade INTEGER,
                    descricao VARCHAR(100)
                )
    ''')
    
    fechamento(conexao)

if __name__ == "__main__":
    criacao_table_user()
    criacao_table_produto()