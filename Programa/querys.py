import sqlite3

def cadastrar_prod(tipo,marca,cor,tamanho,genero,preco,quantidade,descricao):
    conexao = sqlite3.connect('fashion.db')
    
    cursor = conexao.cursor()
    produto = (tipo, marca, tamanho, cor, genero, preco, quantidade, 0, descricao)

    cursor.execute("""
        INSERT INTO Produto (
            tipo, 
            marca, 
            tamanho, 
            cor, 
            genero, 
            preco_unitario, 
            quantidade, 
            promocao, 
            descricao
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
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
    
    conexao.commit()
    conexao.close()
    return list(res)

def selecao_cor():
    conexao = sqlite3.connect('fashion.db')
    
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT cor FROM produto
    """)
    
    res = cursor.fetchall()
    
    conexao.commit()
    conexao.close()
    return list(res)


def atualizar_prod(tipo,marca,cor,tamanho,genero,preco,quantidade,descricao):
    conexao = sqlite3.connect('fashion.db')
    
    cursor = conexao.cursor()
    produto = (tipo, marca, tamanho, cor, genero, preco, quantidade, 0, descricao)

    cursor.execute("""
        
    """, produto)
    
    conexao.commit()
    conexao.close()




