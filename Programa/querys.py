import sqlite3
import os
import pandas as pd
from create_tables import fechamento
import bcrypt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FASHION_DB = os.path.join(BASE_DIR, 'fashion.db')
LOGIN_DB = os.path.join(BASE_DIR, 'LoginUser.db')

def inicializacao():
    conexao = sqlite3.connect(FASHION_DB)
    cursor = conexao.cursor()
    return conexao,cursor

def inicializacao_user():
    conexao = sqlite3.connect(LOGIN_DB)
    cursor = conexao.cursor()
    return conexao,cursor

def fechamento_select(conexao):
    conexao.close()

def cadastrar_prod(tipo,marca,cor,tamanho,genero,preco,quantidade,descricao):
    conexao,cursor = inicializacao()
    produto = (tipo, marca, tamanho, cor, genero, preco, quantidade, descricao)
    cursor.execute("""
        INSERT INTO Produto (
            tipo, 
            marca, 
            tamanho, 
            cor, 
            genero, 
            preco_unitario, 
            quantidade, 
            descricao
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, produto)
    
    fechamento(conexao)

def atualizar_prod(tipo,marca,cor,tamanho,genero,preco,quantidade,descricao):
    conexao,cursor = inicializacao()
    cursor.execute("""
        UPDATE Produto
        SET genero = ?, preco_unitario = ?, quantidade = ? , descricao = ?
        where tipo = ? AND marca = ? AND cor = ? AND tamanho = ?
    """,(genero,preco,quantidade,descricao,tipo,marca,cor, tamanho))
    
    fechamento(conexao)

def selecao_marca():
    conexao,cursor = inicializacao()
    cursor.execute("""
        SELECT marca FROM produto group by marca
    """)
    res = cursor.fetchall()
    fechamento_select(conexao)
    return [linha[0] for linha in res]

def selecao_cor():
    conexao,cursor = inicializacao()
    cursor.execute("""
        SELECT cor FROM produto group by cor
    """)
    res = cursor.fetchall()
    fechamento_select(conexao)
    return [linha[0] for linha in res]

def selecao(tipo, marca, cor, tamanho, genero):
    conexao,_ = inicializacao()
    query = """
        SELECT * FROM Produto 
        WHERE tipo = ? AND marca = ? AND cor = ? AND tamanho = ? AND genero = ?
    """
    df = pd.read_sql_query(query, conexao, params=(tipo, marca, cor, tamanho, genero))
    fechamento_select(conexao)
    return df


def contagem_tipos():
    conexao,cursor = inicializacao()
    cursor.execute("""
        SELECT tipo,COUNT(tipo) FROM produto GROUP BY tipo
    """)
    res = cursor.fetchall()
    fechamento_select(conexao)
    return res

def menor_preco():
    conexao,cursor = inicializacao()
    cursor.execute("""
        SELECT tipo,marca,cor, MIN(preco_unitario) FROM produto
    """)
    res = cursor.fetchall()
    fechamento_select(conexao)
    return res[0]

def validar_login(nome, senha_digitada):
    conexao, cursor = inicializacao_user()
    cursor.execute("""
        SELECT senha FROM Usuario
        WHERE nome = ?
    """, (nome.strip(),))

    resultado = cursor.fetchone()

    conexao.close()

    if resultado:
        hash_salvo = resultado[0].encode()
        return bcrypt.checkpw(senha_digitada.encode(), hash_salvo)
    return False