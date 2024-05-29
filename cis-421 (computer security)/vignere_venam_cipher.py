import string
""" 
1. Assign a number to each character of the plain text and the key according to alphabetical order. 
2. Bitwise XOR both the number (Corresponding plain-text character number and Key character number). 
3. Subtract the number from 26 if the resulting number is greater than or equal to 26, if it isn’t then leave it.
"""
all_letters = string.ascii_letters
def char_pos(char):
    return all_letters.index(char)
def vignere_venam_cipher(plainText, key):
    cipher_text = ''
    correct_key = key
    if len(key) < len(plainText):
        correct_key = key * (len(plainText) - len(key))
    for  p_char, k_char in list(zip(plainText,correct_key)):
        if p_char in all_letters:
            bitwised_digit = char_pos(p_char) ^ char_pos(k_char)
            cipher_text+= all_letters[bitwised_digit % len(all_letters)]
        else: 
            cipher_text+= p_char
    return cipher_text

    
if __name__ == '__main__':
    key = input("provide a given key: ")
    plain_text = input("provide a plain text: ")
    cipher_text = vignere_venam_cipher(plain_text, key)
    print("cipher text: ", cipher_text)
    print("plain text: ", vignere_venam_cipher(cipher_text, key))