import random
import os
import argparse
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



def process_file(input_file, output_file, mode):
    with open(input_file, 'r') as infile:
        text = infile.read()

    cipher_mapping = generate_cipher_mapping()
    if mode == 'encrypt':
        result_text = encrypt(text, cipher_mapping)
    elif mode == 'decrypt':
        result_text = decrypt(text, cipher_mapping)
    else:
        raise ValueError("Mode should be either 'encrypt' or 'decrypt'")

    with open(output_file, 'w') as outfile:
        outfile.write(result_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Encryption and Decryption with a Random Cipher")
    parser.add_argument("input_file", help="Input plaintext file")
    parser.add_argument("output_file", help="Output ciphertext file")
    parser.add_argument("mode", choices=['encrypt', 'decrypt'], help="Mode: encrypt or decrypt")

    args = parser.parse_args()

    # Ensure the input file exists
    if not os.path.exists(args.input_file):
        raise FileNotFoundError(f"The file {args.input_file} does not exist")

    process_file(args.input_file, args.output_file, args.mode)
    print(f"Processed file saved as {args.output_file}")




