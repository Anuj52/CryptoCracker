# caesarCipher.py - Caesar Cipher Encryption/Decryption Program

# Import pyperclip to copy the result to the clipboard (optional, can be removed)
import pyperclip

# The string to be encrypted or decrypted
message = 'This is my secret message.'

# The encryption/decryption key (0 to 25)
key = 13

# Set mode to either 'encrypt' or 'decrypt'
mode = 'encrypt'  # Change to 'decrypt' to decrypt the message

# String of uppercase letters that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Variable to store the encrypted or decrypted message
translated = ''

# Capitalize the message string for uniformity
message = message.upper()

# Run the encryption/decryption process
for symbol in message:
    if symbol in LETTERS:
        # Find the number (index) of the symbol in LETTERS
        num = LETTERS.find(symbol)
        
        # Perform encryption or decryption
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        
        # Handle wrap-around if the number is outside the 0-25 range
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
        
        # Add the encrypted or decrypted letter to the translated message
        translated = translated + LETTERS[num]
    else:
        # Add any symbols (like spaces or punctuation) directly to the message
        translated = translated + symbol

# Print the final translated message
print(translated)

# Copy the translated message to the clipboard (optional)
pyperclip.copy(translated)
