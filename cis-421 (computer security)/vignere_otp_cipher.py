import string
all_letters = string.ascii_letters
# convert all letters to a map of char: index
# for fast access instead of going through the array
all_letters_map = {}
for i in range(len(all_letters)):
    all_letters_map[all_letters[i]] = i
def normalize_key(plaintext, key):
    normalized_key = key
    if len(key) < len(plaintext):
        normalized_key = key * (len(plaintext) - len(key))
    return normalized_key

def decrypt(cipher_text, normalized_key):
    plain_text= ''
    for c_char, k_char in zip(cipher_text, normalized_key):
        if c_char in all_letters:
            index = (all_letters_map[c_char] - all_letters_map[k_char]) % len(all_letters)
            plain_text += all_letters[index]
        else:
            plain_text+= c_char
    return plain_text
def encrypt(plaintext, normalized_key):
     cipher_text= ''
     for p_char, k_char in zip(plaintext, normalized_key):
        if p_char in all_letters:
            index = (all_letters_map[p_char] + all_letters_map[k_char]) % len(all_letters)
            cipher_text += all_letters[index]
        else:
            cipher_text+= p_char
     return cipher_text

def vignere_otp_cipher(text, key, to_encrypt=True):
    normalized_key = normalize_key(text, key)
    if to_encrypt:
        return encrypt(text, normalized_key)
    return decrypt(text, normalized_key)
    
if __name__ == "__main__":
    string = "I love my mum and Dad Very much!"
    keyword = "BiscuIT"
    cipher_text = vignere_otp_cipher(string, keyword)
    plain_text = vignere_otp_cipher(cipher_text, keyword, False)
    print("the cipher text: ", cipher_text)
    print("the plain text: ", plain_text)