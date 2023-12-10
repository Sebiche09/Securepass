"""importe le module unittest pour les tests unitaire"""
import unittest
import string
from password_functions import generate_password, save_password_to_history


class TestPasswordFunctions(unittest.TestCase):
    """ classe comportant des fonctions de test unitaire"""

    def test_generate_password(self):
        """Test unitaire de la fonction generate_password()"""
        generate_password(20, True, True, True)
        with open("password_history.txt", "r", encoding="utf-8") as history_file:
            self.assertIn("TestPassword123!", history_file.read())

    def test_save_password_to_history(self):
        """
        Vérifie que la fonction save_password_to_history ajoute correctement un mot de passe à l'historique.
        PRE :
            - Assurez-vous que 'save_password_to_history' est défini correctement.
        POST :
            - Le mot de passe spécifié est présent dans le fichier d'historique des mots de passe.
        """
        save_password_to_history("TestPassword123!")
        with open("password_history.txt", "r", encoding="utf-8") as history_file:
            self.assertIn("TestPassword123!", history_file.read())

    def test_generate_password_length(self):
        """
        Vérifie que la fonction generate_password génère un mot de passe avec la longueur spécifiée.

        PRE :
            - Assurez-vous que la longueur spécifiée est un entier positif.
        POST :
            - La longueur du mot de passe généré est égale à la longueur spécifiée.
        """
        result = generate_password(10, True, True, True)
        self.assertEqual(len(result), 10)

    def test_generate_password_uppercase(self):
        result = generate_password(8, True, False, False)
        self.assertTrue(any(c.isupper() for c in result))

    def test_generate_password_digits(self):
        result = generate_password(12, False, True, False)
        self.assertTrue(any(c.isdigit() for c in result))

    def test_generate_password_special_characters(self):
        result = generate_password(15, False, False, True)
        self.assertTrue(any(c in string.punctuation for c in result))
if __name__ == '__main__':
    unittest.main()
