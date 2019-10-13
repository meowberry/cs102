def encrypt_caesar(plaintext: str) -> str:
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for x in plaintext:
        if 'a' <= x <= 'z' or 'A' <= x <= 'Z':
            code = ord(x) + 3
            if code > ord('Z') and code < ord('a') or code > ord('z'):
                code -= 26
            ciphertext += chr(code)
        else:
            ciphertext += x
    return ciphertext


def decrypt_caesar(ciphertext: str) -> str:
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for x in ciphertext:
        if 'a' <= x <= 'z' or 'A' <= x <= 'Z':
            code = ord(x) - 3
            if code < ord('a') and code > ord('Z') or code < ord('A'):
                code += 26
            plaintext += chr(code)
        else:
            plaintext += x
    return plaintext
