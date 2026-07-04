import sqlite3
import os
import bcrypt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FASHION_DB = os.path.join(BASE_DIR, 'fashion.db')
LOGIN_DB = os.path.join(BASE_DIR, 'LoginUser.db')

def conexao_login():
    conexao = sqlite3.connect(LOGIN_DB)
    cursor = conexao.cursor()
    return conexao, cursor

def conexao_produto():
    conexao = sqlite3.connect(FASHION_DB)
    cursor = conexao.cursor()
    return conexao, cursor

def fechamento(conexao):
    conexao.commit()
    conexao.close()

def criacao_table_user():
    conexao, cursor = conexao_login()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Usuario(
            id_user INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(50),
            senha VARCHAR(100)
        )
    ''')
    fechamento(conexao)

def criacao_table_produto():
    conexao, cursor = conexao_produto()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Produto(
            id_prod INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo VARCHAR(20),
            marca VARCHAR(50),
            tamanho VARCHAR(10),
            cor VARCHAR(20),
            genero VARCHAR(20),
            preco_unitario FLOAT,
            quantidade INTEGER,
            descricao VARCHAR(100)
        )
    ''')
    fechamento(conexao)

def criar_usuario_padrao(nome="Jose Silva", senha="josias"):
    conexao, cursor = conexao_login()
    cursor.execute("SELECT 1 FROM Usuario WHERE nome = ?", (nome,))
    if not cursor.fetchone():
        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        cursor.execute(
            "INSERT INTO Usuario (nome, senha) VALUES (?, ?)",
            (nome, senha_hash.decode())
        )
    fechamento(conexao)

def inicializar_bancos():
    criacao_table_user()
    criacao_table_produto()
    criar_usuario_padrao()

if __name__ == "__main__":
    inicializar_bancos()