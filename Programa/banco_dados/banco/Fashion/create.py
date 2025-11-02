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

def criacao_informacoes_venda():
    conexao = sqlite3.connect("fashion.db")
    
    cursor = conexao.cursor()
    
    cursor.execute('''
                CREATE TABLE Venda(
                    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
                    data_venda DATETIME,
                    preco_unitario FLOAT,
                    quantidade_vendida INTEGER,
                    preco_total FLOAT
                )
    ''')
    
    conexao.commit()
    conexao.close()


def criacao_pessoa_comprante():
    conexao = sqlite3.connect("fashion.db")
    
    cursor = conexao.cursor()
    
    cursor.execute('''
                CREATE TABLE Pessoa(
                    id_pessoa INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(100),
                    CPF VARCHAR(20),
                    id_prodfk INTEGER,
                    id_vendafk INTEGER,
                    FOREIGN KEY (id_prodfk) REFERENCES Produto(id_prod),
                    FOREIGN KEY (id_vendafk) REFERENCES Venda(id_venda)
                )
    ''')
    
    conexao.commit()
    conexao.close()


if __name__ == "__main__":
    criacao_produto()
    criacao_informacoes_venda()
    criacao_pessoa_comprante()