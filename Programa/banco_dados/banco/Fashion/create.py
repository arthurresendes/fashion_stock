import sqlite3


def criacao_produto():
    conexao = sqlite3.connect("fashion.db")
    
    cursor = conexao.cursor()
    
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
                    promocao BOOL,
                    descricao VARCHAR(100)
                )
    ''')
    
    conexao.commit()
    conexao.close()
    


if __name__ == "__main__":
    criacao_produto()
