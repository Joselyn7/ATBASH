def atbash_decrypt(text):
    decrypted_text = ""
    for char in text:
        if 'A' <= char <= 'Z':
            decrypted_text += chr(90 - (ord(char) - 65))
        elif 'a' <= char <= 'z':
            decrypted_text += chr(122 - (ord(char) - 97))
        else:
            decrypted_text += char

    return decrypted_text