import string


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