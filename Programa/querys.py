import sqlite3
import pandas as pd

def cadastrar_prod(tipo,marca,cor,tamanho,genero,preco,quantidade,descricao):
    conexao = sqlite3.connect('fashion.db')
    
    cursor = conexao.cursor()
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
    
    conexao.commit()
    conexao.close()


def selecao_marca():
    conexao = sqlite3.connect('fashion.db')
    
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT marca FROM produto
    """)
    
    res = cursor.fetchall()
    
    conexao.close()
    return [linha[0] for linha in res]

def selecao_cor():
    conexao = sqlite3.connect('fashion.db')
    
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT cor FROM produto
    """)
    
    res = cursor.fetchall()
    
    conexao.close()
    return [linha[0] for linha in res]


def atualizar_prod(tipo,marca,cor,tamanho,genero,preco,quantidade,descricao):
    conexao = sqlite3.connect('fashion.db')
    
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE Produto
        SET genero = ?, preco_unitario = ?, quantidade = ? , descricao = ?
        where tipo = ? AND marca = ? AND cor = ? AND tamanho = ?
    """,(genero,preco,quantidade,descricao,tipo,marca,cor, tamanho))
    
    conexao.commit()
    conexao.close()



def selecao(tipo, marca, cor, tamanho, genero):
    conexao = sqlite3.connect('fashion.db')

    query = """
        SELECT * FROM Produto 
        WHERE tipo = ? AND marca = ? AND cor = ? AND tamanho = ? AND genero = ?
    """

    df = pd.read_sql_query(query, conexao, params=(tipo, marca, cor, tamanho, genero))

    conexao.close()

    return df


def contagem_tipos():
    conexao = sqlite3.connect('fashion.db')
    
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT tipo,COUNT(tipo) FROM produto GROUP BY tipo
    """)
    
    res = cursor.fetchall()
    
    conexao.close()
    return res

print(contagem_tipos())