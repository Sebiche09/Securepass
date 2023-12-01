import argparse
import string
import secrets
import pyperclip
import os

PASSWORD_HISTORY_FILE = "password_history.txt"

def generate_password(length, uppercase, digits, special):
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
    with open(PASSWORD_HISTORY_FILE, 'a') as history_file:
        history_file.write(f'{password}\n')

def main():
    parser = argparse.ArgumentParser(description='Générateur de mots de passe sécurisés.')
    parser.add_argument('--length', type=int, default=12, help='Longueur du mot de passe.')
    parser.add_argument('--uppercase', action='store_true', help='Inclure des majuscules.')
    parser.add_argument('--no-uppercase', dest='uppercase', action='store_false', help='Exclure des majuscules.')
    parser.add_argument('--digits', action='store_true', help='Inclure des chiffres.')
    parser.add_argument('--no-digits', dest='digits', action='store_false', help='Exclure des chiffres.')
    parser.add_argument('--special', action='store_true', help='Inclure des caractères spéciaux.')
    parser.add_argument('--no-special', dest='special', action='store_false', help='Exclure des caractères spéciaux.')

    args = parser.parse_args()
    generate_password(args.length, args.uppercase, args.digits, args.special)

if __name__ == '__main__':
    main()
