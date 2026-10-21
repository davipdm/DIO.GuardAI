"""Versão corrigida do laboratório: valores separados do comando SQL.

Não é autenticação de produção: dados fictícios e senhas didáticas em memória.
"""

from lab.app import create_database


def login(connection, username, password):
    query = "SELECT username FROM users WHERE username = ? AND password = ?"
    return connection.execute(query, (username, password)).fetchone() is not None


if __name__ == "__main__":
    database = create_database()
    try:
        print("Login correto:", login(database, "aluno", "senha-ficticia"))
        print("Senha incorreta:", login(database, "aluno", "errada"))
        print("Entrada de laboratório:", login(database, "aluno' -- ", "errada"))
    finally:
        database.close()
