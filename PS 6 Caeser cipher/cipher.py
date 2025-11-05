def cipher(text,shift,mode='encrypt'):
    result = ''

    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'

            result += chr((ord(char)-ord(base)+shift)%26+ ord(base) )

        else:
            result += char
    return result
    
text = "Hello World!"
shift = 4

enc = cipher(text, shift, 'encrypt')
dec = cipher(enc, shift, 'decrypt')

print("Encrypted text:", enc)
print("Decrypted text:", dec)