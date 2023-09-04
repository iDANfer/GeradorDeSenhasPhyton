import secrets
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
while True:
    password_length = int(input("Digite o comprimento da senha desejada: "))
    password = generate_random_password(password_length)
    print("Senha gerada:", password)
    import secrets
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
while True:
    password_length = int(input("Digite o comprimento da senha desejada: "))
    password = generate_random_password(password_length)
    print("Senha gerada:", password)
    continue