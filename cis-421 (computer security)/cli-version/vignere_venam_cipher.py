import string
import argparse
import os

all_letters = string.ascii_letters

def char_pos(char):
    return all_letters.index(char)

def normalize_key(text, key):
    normalized_key = key
    if len(key) < len(text):
        normalized_key = (key * ((len(text) // len(key)) + 1))[:len(text)]
    return normalized_key

def vignere_venam_cipher(text, key, to_encrypt=True):
    cipher_text = ''
    normalized_key = normalize_key(text, key)
    for t_char, k_char in zip(text, normalized_key):
        if t_char in all_letters:
            bitwised_digit = char_pos(t_char) ^ char_pos(k_char)
            cipher_text += all_letters[bitwised_digit % len(all_letters)]
        else:
            cipher_text += t_char
    return cipher_text

def process_file(input_file, output_file, key, mode):
    with open(input_file, 'r') as infile:
        text = infile.read()

    if mode == 'encrypt':
        result_text = vignere_venam_cipher(text, key, to_encrypt=True)
    elif mode == 'decrypt':
        result_text = vignere_venam_cipher(text, key, to_encrypt=False)
    else:
        raise ValueError("Mode should be either 'encrypt' or 'decrypt'")

    with open(output_file, 'w') as outfile:
        outfile.write(result_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vigenère-Vernam Cipher File Encryption and Decryption")
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
