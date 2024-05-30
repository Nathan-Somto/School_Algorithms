import string
import argparse
import os

all_letters = string.ascii_letters
# Convert all letters to a map of char: index for fast access
all_letters_map = {all_letters[i]: i for i in range(len(all_letters))}

def normalize_key(plaintext, key):
    normalized_key = key
    if len(key) < len(plaintext):
        normalized_key = (key * ((len(plaintext) // len(key)) + 1))[:len(plaintext)]
    return normalized_key

def decrypt(cipher_text, normalized_key):
    plain_text = ''
    for c_char, k_char in zip(cipher_text, normalized_key):
        if c_char in all_letters:
            index = (all_letters_map[c_char] - all_letters_map[k_char]) % len(all_letters)
            plain_text += all_letters[index]
        else:
            plain_text += c_char
    return plain_text

def encrypt(plaintext, normalized_key):
    cipher_text = ''
    for p_char, k_char in zip(plaintext, normalized_key):
        if p_char in all_letters:
            index = (all_letters_map[p_char] + all_letters_map[k_char]) % len(all_letters)
            cipher_text += all_letters[index]
        else:
            cipher_text += p_char
    return cipher_text

def vignere_otp_cipher(text, key, to_encrypt=True):
    normalized_key = normalize_key(text, key)
    if to_encrypt:
        return encrypt(text, normalized_key)
    return decrypt(text, normalized_key)

def process_file(input_file, output_file, key, mode):
    with open(input_file, 'r') as infile:
        text = infile.read()

    if mode == 'encrypt':
        result_text = vignere_otp_cipher(text, key, to_encrypt=True)
    elif mode == 'decrypt':
        result_text = vignere_otp_cipher(text, key, to_encrypt=False)
    else:
        raise ValueError("Mode should be either 'encrypt' or 'decrypt'")

    with open(output_file, 'w') as outfile:
        outfile.write(result_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vigenère Cipher File Encryption and Decryption")
    parser.add_argument("input_file", help="Input file to be encrypted or decrypted")
    parser.add_argument("output_file", help="Output file to save the result")
    parser.add_argument("key", help="Encryption/Decryption key")
    parser.add_argument("mode", choices=['encrypt', 'decrypt'], help="Mode: encrypt or decrypt")

    args = parser.parse_args()

    # Ensure the input file exists
    if not os.path.exists(args.input_file):
        raise FileNotFoundError(f"The file {args.input_file} does not exist")

    # Process the file
    process_file(args.input_file, args.output_file, args.key, args.mode)
    print(f"Processed file saved as {args.output_file}")
