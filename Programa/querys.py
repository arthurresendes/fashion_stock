import sqlite3

def cadastrar_prod(tipo,marca,cor,tamanho,genero,preco,quantidade,descricao):
    conexao = sqlite3.connect('fashion.db')
    
    cursor = conexao.cursor()
    produto = (tipo,marca,cor,tamanho,genero,preco,quantidade,descricao)
    cursor.execute("INSERT INTO Produto(tipo,marca,cor,tamanho,genero,preco,quantidade,descricao) VALUES (?,?,?,?,?,?,?,?)", produto)
    
    conexao.commit()
    conexao.close


