# caesar_cipher.py

"""
This program implements the Caesar cipher encryption technique.
It shifts letters in the message by a specified key.
"""

# --- Imports ---
import pyperclip  # To copy the result to the clipboard

# --- Constants ---
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_cipher(message: str, key: int) -> str:
    """
    Encrypts a message using the Caesar cipher.

    Parameters:
    - message (str): The message to encrypt.
    - key (int): The shift value for encryption.

    Returns:
    - str: The encrypted message.
    """
    translated = ''  # Initialize the encrypted message
    
    for symbol in message:
        if symbol.isalpha():  # Check if the symbol is a letter
            # Shift the letter and wrap around the alphabet
            shifted_index = (ALPHABET.index(symbol.upper()) + key) % 26
            translated += ALPHABET[shifted_index]  # Append the translated letter
        else:
            translated += symbol  # Non-letter characters are unchanged
            
    return translated

# --- Main Program ---
if __name__ == '__main__':
    message = input("Enter the message: ")  # Get user input
    key = int(input("Enter the shift key: "))  # Get shift key
    encrypted_message = caesar_cipher(message, key)  # Encrypt the message
    print(f'Encrypted Message: {encrypted_message}')  # Display result
    pyperclip.copy(encrypted_message)  # Copy to clipboard
