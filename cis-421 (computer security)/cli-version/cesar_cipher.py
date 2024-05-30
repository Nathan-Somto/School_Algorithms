import string
import argparse
import os

def caesar_cipher(text,n):
    chars = string.ascii_letters;
    # ensures that n is not above 26;
    n = n % 26;
    # create a dictionary of plain text(as key): cipher text(as value);
    pairs = {};
    for i in range(len(chars)):
        char = chars[i];
        result = ord(char) + n;
        if char.islower() and result > 122:
            result -= 26
        if char.isupper() and result > 90:
            result -= 26
        pairs[char] = chr(result);
    c = ''
    for char in text:
        if char in pairs:
            c += pairs[char]
    else:
        c += char
    return c
 
def process_file(input_file, output_file, shift, mode):
    with open(input_file, 'r') as infile:
        text = infile.read()
    
    if mode == 'encrypt':
        result_text = caesar_cipher(text, shift)
    elif mode == 'decrypt':
        result_text = caesar_cipher(text, -shift)
    else:
        raise ValueError("Mode should be either 'encrypt' or 'decrypt'")
    
    with open(output_file, 'w') as outfile:
        outfile.write(result_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Caesar Cipher encryption and decryption")
    parser.add_argument("input_file", help="Input plaintext file")
    parser.add_argument("output_file", help="Output ciphertext file")
    parser.add_argument("shift", type=int, help="Shift digit for the Caesar Cipher")
    parser.add_argument("mode", choices=['encrypt', 'decrypt'], help="Mode: encrypt or decrypt")

    args = parser.parse_args()

    # Ensure the input file exists
    if not os.path.exists(args.input_file):
        raise FileNotFoundError(f"The file {args.input_file} does not exist")

    process_file(args.input_file, args.output_file, args.shift, args.mode)
    print(f"Processed file saved as {args.output_file}")