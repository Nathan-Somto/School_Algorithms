import math
import random
import argparse
import os
def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b, a%b)
def generate_prime():
    number = random.randrange(1_000_000_000, 1_000_000_000_000)
    while not is_prime(number):
        number = random.randrange(1_000_000_000, 1_000_000_000_000)
    return number
def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(number) + 1)):
        if  number % i == 0:
            return False
    return True
def get_e(phi ,start=2):
    while True:
        if gcd(phi, start) == 1:
            return start
        start += 1

def x_gcd(a, b):
    b, x0, x1 = b, 0, 1
    while a > 1:
        quotient = a // b
        b, a = a % b, b
        x0, x1 = x1 - quotient * x0, x0
    if x1 < 0 :
        return x1 + b 
    return x1
   
def rsa_key_pair():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p-1) * (q - 1)
    e = get_e(phi)
    d = x_gcd(e, phi)
    return ((e, n), (d, n))
def read_key(key_file):
    with open(key_file, 'r') as kf:
        key = tuple(map(int, kf.read().split(',')))
    return key

def write_key(key, key_file):
    with open(key_file, 'w') as kf:
        kf.write(','.join(map(str, key)))
def rsa_encrypt(plain_text, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plain_text]
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join(chr(pow(char, d, n)) for char in ciphertext)
def process_file(input_file, output_file, key, mode):
    with open(input_file, 'r') as infile:
        text = infile.read()

    if mode == 'encrypt':
        encrypted_data = rsa_encrypt(text, key)
        with open(output_file, 'w') as outfile:
            outfile.write(' '.join(map(str, encrypted_data)))
    elif mode == 'decrypt':
        with open(input_file, 'r') as infile:
            encrypted_data = list(map(int, infile.read().split()))
        decrypted_text = rsa_decrypt(encrypted_data, key)
        with open(output_file, 'w') as outfile:
            outfile.write(decrypted_text)
    else:
        raise ValueError("Mode should be either 'encrypt' or 'decrypt'")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RSA File Encryption and Decryption")
    parser.add_argument("input_file", help="Input file to be encrypted or decrypted")
    parser.add_argument("output_file", help="Output file to save the result")
    parser.add_argument("mode", choices=['encrypt', 'decrypt'], help="Mode: encrypt or decrypt")
    parser.add_argument("--public_key", help="File containing the public key (e,n)")
    parser.add_argument("--private_key", help="File containing the private key (d,n)")
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        raise FileNotFoundError(f"The file {args.input_file} does not exist")

    if args.public_key and args.private_key:
        public_key = read_key(args.public_key)
        private_key = read_key(args.private_key)
    else:
        public_key, private_key = rsa_key_pair()
        print("Generated Public Key:", public_key)
        print("Generated Private Key:", private_key)

       
        with open('public_key.txt', 'w') as f:
             f.write(','.join(map(str, public_key)))
        with open('private_key.txt', 'w') as f:
            f.write(','.join(map(str, private_key)))

    # Select the correct key based on the mode
    key = public_key if args.mode == 'encrypt' else private_key
    
    # Process the file
    process_file(args.input_file, args.output_file, key, args.mode)
    print(f"Processed file saved as {args.output_file}")