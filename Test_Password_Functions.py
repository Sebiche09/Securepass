import unittest
from Password_Functions import generate_password, save_password_to_history, main_password

class TestPasswordFunctions(unittest.TestCase):

    def test_generate_password(self):
        generate_password(20, True, True, True)
        with open("password_history.txt", "r") as history_file:
            self.assertIn("TestPassword123!", history_file.read())

    def test_save_password_to_history(self):
        save_password_to_history("TestPassword123!")
        with open("password_history.txt", "r") as history_file:
            self.assertIn("TestPassword123!", history_file.read())
if __name__ == '__main__':
    unittest.main()
