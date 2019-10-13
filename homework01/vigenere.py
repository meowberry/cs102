def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    keyword *= len(plaintext) // len(keyword) + 1
    i = 0
    for ch in plaintext:
        if keyword[i].isupper():
            shift = ord(keyword[i]) - 65
        elif keyword[i].islower():
            shift = ord(keyword[i]) - 97
        if ch.isupper():
            ciphertext += chr((ord(ch) + shift - 65) % 26 + 65)
        elif ch.islower():
            ciphertext += chr((ord(ch) + shift - 97) % 26 + 97)
        i += 1

    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    keyword *= len(ciphertext) // len(keyword) + 1
    i = 0
    for ch in ciphertext:
        if keyword[i].isupper():
            shift = ord(keyword[i]) - 65
        elif keyword[i].islower():
            shift = ord(keyword[i]) - 97
        if ch.isupper():
            plaintext += chr((ord(ch) - shift - 65) % 26 + 65)
        elif ch.islower():
            plaintext += chr((ord(ch) - shift - 97) % 26 + 97)
        i += 1

    return plaintext
