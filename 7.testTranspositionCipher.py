# Test Transposition Cipher Encryption and Decryption

import math
import pyperclip

def encryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * numOfColumns

    col = 0
    row = 0

    for symbol in message:
        ciphertext[col] += symbol
        col += 1

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row.
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(ciphertext)

def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = [''] * numOfColumns

    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1

        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)

def testCipher():
    messages = [
        "Common sense is not so common.",
        "The quick brown fox jumps over the lazy dog.",
        "To be or not to be, that is the question.",
        "All that glitters is not gold.",
        "A journey of a thousand miles begins with a single step."
    ]

    keys = [5, 6, 7, 8, 10]

    for message in messages:
        for key in keys:
            print(f"Testing message: {message} with key: {key}")
            encrypted = encryptMessage(key, message)
            decrypted = decryptMessage(key, encrypted)

            # Check if the decrypted message matches the original message
            if message == decrypted:
                print(f"Success! The decrypted message matches the original.\n")
            else:
                print(f"Failure! The decrypted message does NOT match the original.\n")

if __name__ == '__main__':
    testCipher()
