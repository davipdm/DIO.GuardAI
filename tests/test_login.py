"""Regressão comportamental de SQL Injection em SQLite descartável."""

import unittest

from app import login
from lab.app import create_database, login as vulnerable_login


class LoginTests(unittest.TestCase):
    def setUp(self):
        self.database = create_database()
        self.addCleanup(self.database.close)

    def test_valid_credentials(self):
        self.assertTrue(login(self.database, "aluno", "senha-ficticia"))

    def test_wrong_password(self):
        self.assertFalse(login(self.database, "aluno", "errada"))

    def test_unknown_user(self):
        self.assertFalse(login(self.database, "desconhecido", "senha-ficticia"))

    def test_reproduce_original_bypass(self):
        for username in ("aluno' -- ", "aluno' --"):
            with self.subTest(username=username):
                self.assertTrue(vulnerable_login(self.database, username, "errada"))

    def test_username_injection_is_rejected(self):
        for username in ("aluno' -- ", "aluno' --", "' OR 1=1 -- "):
            with self.subTest(username=username):
                self.assertFalse(login(self.database, username, "errada"))

    def test_password_injection_is_rejected(self):
        self.assertFalse(login(self.database, "aluno", "' OR '1'='1"))

    def test_apostrophe_is_literal_data(self):
        self.database.execute(
            "INSERT INTO users VALUES (?, ?)", ("d'ávila", "senha'local")
        )
        self.assertTrue(login(self.database, "d'ávila", "senha'local"))
        self.assertFalse(login(self.database, "d'ávila", "errada"))

    def test_empty_input(self):
        self.assertFalse(login(self.database, "", ""))


if __name__ == "__main__":
    unittest.main()
