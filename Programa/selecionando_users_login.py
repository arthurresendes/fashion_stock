import sqlite3

def lista_usuarios():
    conexao  = sqlite3.connect("LoginUser.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT nome,senha FROM Usuario")
    
    res = cursor.fetchall()
    lista_users = []
    for result in res:
        lista_users.append(result)
    
    conexao.commit()
    conexao.close()

    return lista_users


if __name__ == "__main__":
    lista_usuarios()