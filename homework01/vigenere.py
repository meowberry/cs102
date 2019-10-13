def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    for index, x in enumerate(plaintext):
        if 'a' <= x <= 'z' or 'A' <= x <= 'Z':
            shift = ord(keyword[index % len(keyword)])
            shift -= ord('a') if 'a' <= x <= 'z' else ord('A')
            code = ord x) + shift
            if 'a' <= x <= 'z' and code > ord('z'):
                code -= 26
            elif 'A' <= x <= 'Z' and code > ord('Z'):
                code -= 26
            ciphertext += chr(code)
        else:
            chiphertext += x
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext=''
    for index, x in enumerate(ciphertext):
        if 'a' <= x <= 'z' or 'A' <= x <= 'Z':
            shift=ord(keyword[index % len(keyword)])
            shift -= ord('a') if 'a' <= x <= 'z' else ord('A')
            code=ord x) - shift
            if 'a' <= x <= 'z' and code < ord('a'):
                code += 26
            elif 'A' <= x <= 'Z' and code < ord('A'):
                code += 26
            plaintext += chr(code)
        else:
            plaintext += x
    return plaintext
