import math
import random
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

def rsa_encrypt(plain_text, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plain_text]
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join(chr(pow(char, d, n)) for char in ciphertext)
if __name__ == "__main__":
   plain_text = "Biscuit"
   public_key, private_key = rsa_key_pair()
   print("public_key: ", public_key)
   print("private key:", private_key)
   cipher_text = rsa_encrypt(plain_text, public_key)
   print("cipher text: ", cipher_text)
   print("plain text: ", rsa_decrypt(cipher_text,private_key))

