"""importe le module unittest pour les tests unitaire"""
import unittest
from password_functions import generate_password, save_password_to_history


class TestPasswordFunctions(unittest.TestCase):
    """ classe comportant des fonctions de test unitaire"""
    def test_generate_password(self):
        """Test unitaire de la fonction generate_password()"""
        generate_password(20, True, True, True)
        with open("password_history.txt", "r", encoding="utf-8") as history_file:
            self.assertIn("TestPassword123!", history_file.read())

    def test_save_password_to_history(self):
        """Test unitaire de la fonction save_password_to_history()"""
        save_password_to_history("TestPassword123!")
        with open("password_history.txt", "r", encoding="utf-8") as history_file:
            self.assertIn("TestPassword123!", history_file.read())


if __name__ == '__main__':
    unittest.main()
