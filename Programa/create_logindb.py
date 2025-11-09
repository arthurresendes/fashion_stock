import sqlite3


def criacao():
    conexao = sqlite3.connect("LoginUser.db")
    
    cursor = conexao.cursor()
    
    cursor.execute('''
                CREATE TABLE Usuario(
                    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(50),
                    senha VARCHAR(30)
                )
    ''')
    
    conexao.commit()
    conexao.close()


if __name__ == "__main__":
    criacao()