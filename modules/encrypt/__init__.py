"This module is for encrypting and decrypting files"

def encrypt_file(input_file, output_file, password: int = 3):
    with open(input_file, 'r') as file:
        plain_text = file.read()
    # plain_text = plain_text.replace(" ", "iLqyC;")
    plain_text = plain_text.replace("\n", "")
    encrypt_text = encrypt(plain_text, password)
    with open(output_file, 'w') as file:
        file.write(encrypt_text)

        print('done encrypt')

def decrypt_file(input_file, output_file, password: int = 3):
    with open(input_file, 'r') as file:
        encrypt_text = file.read()
    
    decrypt_text = decrypt(encrypt_text, password)
    with open(output_file, 'w') as file:
        file.write(decrypt_text)
    print('done decrypt')
    
def encrypt(text, password: int = 3):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord("A")
            encrypted_char = chr((ord(char) - ascii_offset + password) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypt_text, password):
    return encrypt(encrypt_text, -password)