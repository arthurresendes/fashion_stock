import sqlite3
import secrets


def insercao_user():
    conexao  = sqlite3.connect("LoginUser.db")
    cursor = conexao.cursor()
    
    lista_usuarios = [("Arthur Resende",secrets.token_hex(8)),("Maria Clara", secrets.token_hex(16)),("Jose Silva", secrets.token_hex(4))]
    
    cursor.executemany("INSERT INTO Usuario (nome , senha) VALUES (?,?)", lista_usuarios)
    
    conexao.commit()
    conexao.close()


if __name__ == "__main__":
    insercao_user()