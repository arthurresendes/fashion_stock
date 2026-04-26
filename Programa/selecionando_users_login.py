import sqlite3
import hashlib

def validar_login(nome, senha_digitada):
    conexao = sqlite3.connect("LoginUser.db")
    cursor = conexao.cursor()

    hash_senha = hashlib.md5(senha_digitada.encode()).hexdigest()
    cursor.execute("""
        SELECT * FROM Usuario
        WHERE nome = ? AND senha = ?
    """, (nome, hash_senha))

    usuario = cursor.fetchone()

    conexao.close()

    if usuario:
        return True
    else:
        return False