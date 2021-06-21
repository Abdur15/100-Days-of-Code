alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import logo
logo = logo.logo
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text = text , shift = shift):
    enc = ""
    for i in text:
        if i not in alphabet:
            enc += i
        else:
            a = alphabet.index(i)
            d = a + shift
            if d > 25:
                b = alphabet[d - 26]
                c = alphabet.index(b)
                enc += alphabet[c]
            else:
                b = alphabet[d]
                c = alphabet.index(b)
                enc += alphabet[c]
    print(enc)

def decrypt(text = text , shift = shift):
    dec = ""
    for i in text:
        if i not in alphabet:
            dec += i
        else:
            a = alphabet.index(i)
            d = a - shift
            b = alphabet[d]
            c = alphabet.index(b)
            dec += alphabet[c]
    print(dec)
if direction == 'encode':
    encrypt()
    f = input("If you want to continue\npress y if not press n").lower()
    if f == 'y':
        text1 = input("Type your message:\n").lower()
        decrypt(text = text1)
else:
    decrypt()

