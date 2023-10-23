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

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)


plaintext = 'Hello, World!'
shift = 3
encrypted_text1 = encrypt(plaintext, shift)
print(encrypted_text1)

encrypted_text2 = decrypt(encrypted_text1, shift)
print(encrypted_text2)