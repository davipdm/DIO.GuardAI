"""Login propositalmente vulnerável. Apenas laboratório local, sem servidor."""

import sqlite3


def create_database():
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE users (username TEXT, password TEXT)")
    connection.execute(
        "INSERT INTO users VALUES (?, ?)", ("aluno", "senha-ficticia")
    )
    return connection


def login(connection, username, password):
    # Exercício: onde termina o dado digitado e começa a instrução SQL?
    query = (
        "SELECT username FROM users "
        f"WHERE username = '{username}' AND password = '{password}'"
    )
    return connection.execute(query).fetchone() is not None


if __name__ == "__main__":
    database = create_database()
    try:
        print("Login correto:", login(database, "aluno", "senha-ficticia"))
        print("Senha incorreta:", login(database, "aluno", "errada"))
        print("Entrada de laboratório:", login(database, "aluno' -- ", "errada"))
    finally:
        database.close()
