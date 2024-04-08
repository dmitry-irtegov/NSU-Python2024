import argparse

from affinecipher.ciphertable import CipherTable


def decrypt(text: str, key: str) -> str:
    # TODO: language selection
    table = CipherTable(key)
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            encrypted_text += table.decrypt(char)
        else:
            encrypted_text += char
    return encrypted_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
