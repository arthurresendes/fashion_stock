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



def selecao(tipo,marca,cor,tamanho,genero):
    conexao = sqlite3.connect('fashion.db')
    
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM Produto where tipo = ? AND marca = ? AND cor = ? AND tamanho = ? AND genero = ?
    """,(tipo,marca,cor,tamanho,genero))
    
    
    res = cursor.fetchall()
    df = pd.read_sql_query(res,conexao)
    df.to_excel("resultados_pesquisa", index=False, sheet_name='Resultados')
    conexao.close()
    return df