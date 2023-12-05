"""module"""
import argparse
import string
import secrets
import pyperclip

PASSWORD_HISTORY_FILE = "password_history.txt"


def generate_password(length, uppercase, digits, special):
    """
    Génère un mot de passe en fonction des critères spécifiés.
    PRE :
        Length est un entier positif
        Au moins un des paramètres uppercase, digits, special est True

    POST :
        Le mot de passe généré est copié dans le presse-papiers
        Le mot de passe généré est affiché
        Le mot de passe généré est enregistré dans l'historique
    """

    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special:
        characters += string.punctuation

    generated_password = ''.join(secrets.choice(characters) for _ in range(length))

    # Copie le mot de passe dans le presse-papiers
    pyperclip.copy(generated_password)

    # Affiche le mot de passe généré
    print(f'Mot de passe généré: {generated_password}')
    print('Le mot de passe a été copié dans le presse-papiers.')

    # Enregistre le mot de passe dans l'historique
    save_password_to_history(generated_password)


def save_password_to_history(password):
    """
     Ajoute le mot de passe spécifié à l'historique des mots de passe.

    PRE : password est une chaîne de caractères non vide

    POST : le mot de passe est ajouté à l'historique
     """
    with open(PASSWORD_HISTORY_FILE, 'a', encoding="utf-8") as history_file:
        history_file.write(f'{password}\n')


def main_password():
    """
    Fonction principale du programme.

    PRE : Aucune précondition particulière.

    POST :
    - Récupère les paramètres de la ligne de commande, tels que la longueur du mot de passe,
      l'inclusion/exclusion des majuscules, des chiffres et des caractères spéciaux.
    - Utilise les paramètres récupérés pour générer un mot de passe sécurisé.
    """
    parser = argparse.ArgumentParser(description='Générateur de mots de passe sécurisés.')
    parser.add_argument('--length', type=int, default=12,
                        help='Longueur du mot de passe.')
    parser.add_argument('--uppercase', action='store_true',
                        help='Inclure des majuscules.')
    parser.add_argument('--no-uppercase', dest='uppercase', action='store_false',
                        help='exclure des majuscules.')
    parser.add_argument('--digits', action='store_true', help='Inclure des chiffres.')
    parser.add_argument('--no-digits', dest='digits', action='store_false',
                        help='Exclure des chiffres.')
    parser.add_argument('--special', action='store_true',
                        help='Inclure des caractères spéciaux.')
    parser.add_argument('--no-special', dest='special', action='store_false',
                        help='Exclure des caractères spéciaux.')

    args = parser.parse_args()
    generate_password(args.length, args.uppercase, args.digits, args.special)
