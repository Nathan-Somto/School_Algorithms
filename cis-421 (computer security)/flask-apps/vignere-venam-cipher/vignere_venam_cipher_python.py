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