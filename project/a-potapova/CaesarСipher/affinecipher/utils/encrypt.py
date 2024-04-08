import argparse

from affinecipher.ciphertable import CipherTable


def encrypt(text: str, key: str) -> str:
    # TODO: language selection
    table = CipherTable(key)
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            encrypted_text += table.encrypt(char)
        else:
            encrypted_text += char
    return encrypted_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
