def encrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        plain_text = file.read()
    # plain_text = plain_text.replace(" ", "")
    plain_text = plain_text.replace("\n", "")
    encrypt_text = encrypt(plain_text, shift)
    with open(output_file, 'w') as file:
        file.write(encrypt_text)

        print('done encrypt')

def decrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        encrypt_text = file.read()
    
    decrypt_text = decrypt(encrypt_text, shift)
    with open(output_file, 'w') as file:
        file.write(decrypt_text)
    print('done decrypt')
    
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord("A")
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypt_text, shift):
    return encrypt(encrypt_text, -shift)



# input_file = "index.html"
# output_file = "main2.txt"
# shift = 1000

# encrypt_file(input_file, output_file, shift)



input_file = "main2.txt"
output_file = "main3.html"
shift = 1000

decrypt_file(input_file, output_file, shift)
