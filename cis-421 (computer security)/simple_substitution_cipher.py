import random

def generate_cipher_mapping():
    ascii_chars = [chr(i) for i in range(32, 127)]  
    random.shuffle(ascii_chars)
    cipher_mapping = {chr(i): ascii_chars[i - 32] for i in range(32, 127)}
    return cipher_mapping

def encrypt(message, cipher_mapping):
    encrypted_message = ''.join(cipher_mapping.get(char, char) for char in message)
    return encrypted_message

def decrypt(encrypted_message, cipher_mapping):
    inverse_mapping = {value: key for key, value in cipher_mapping.items()}
    decrypted_message = ''.join(inverse_mapping.get(char, char) for char in encrypted_message)
    return decrypted_message


message = "I love my dad and mum very much!"
cipher_mapping = generate_cipher_mapping()

encrypted_message = encrypt(message, cipher_mapping)
print("Encrypted message:", encrypted_message)


decrypted_message = decrypt(encrypted_message, cipher_mapping)
print("Decrypted message:", decrypted_message)




