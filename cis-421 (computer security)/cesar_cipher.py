import string
text = string.ascii_letters;
n = int(input("Enter shift digit: "));
# ensures that n is not above 26;
n = n % 26;
# create a dictionary of plain text(as key): cipher text(as value);
pairs = {};
for i in range(len(text)):
    char = text[i];
    result = ord(char) + n;
    if char.islower() and result > 122:
        result -= 26
    if char.isupper() and result > 90:
        result -= 26
    pairs[char] = chr(result);
p = input("enter plain text: ");
c = ''
for char in p:
    if char in pairs:
        c += pairs[char]
    else:
        c += char

print("cipher text: ", c) 