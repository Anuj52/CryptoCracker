# transposition_cipher.py
# This program encrypts a message using the Transposition Cipher.
# The Transposition Cipher rearranges characters in the message
# based on a defined key, making the original message unreadable.

# Function to encrypt the message using Transposition Cipher
def encrypt_message(message, key):
    # Step 1: Prepare a list to hold each column of characters
    columns = [''] * key
    
    # Step 2: Populate the columns with characters from the message
    for index, character in enumerate(message):
        column_index = index % key  # Determine which column to place the character
        columns[column_index] += character  # Append character to the appropriate column
    
    # Step 3: Combine the columns to create the ciphertext
    ciphertext = ''.join(columns)
    return ciphertext

# Main function to execute the program
if __name__ == '__main__':
    # Step 4: Define the message and key
    message = "Common sense is not so common."
    key = 8  # Number of columns for the Transposition Cipher

    # Step 5: Call the encryption function and display the result
    encrypted_message = encrypt_message(message, key)
    print("Ciphertext:", encrypted_message)

'''-------------------------------------------------------------------------------------------------------------------'''

# Note: This code assumes that spaces and punctuation are included in the message
# and that the output will maintain these characters.

# transpositionEncrypt.py
# This program encrypts a message using the Transposition Cipher.
# The Transposition Cipher rearranges characters in the message
# based on a defined key, making the original message unreadable.

'''----------------------------------------------------------------------------------------------------------------------------------'''

import pyperclip  # Importing pyperclip to copy the encrypted message to the clipboard

def main():
    # Step 1: Define the message and key for encryption
    myMessage = 'Common sense is not so common.'
    myKey = 8  # Number of columns for the Transposition Cipher

    # Step 2: Call the encryption function and store the ciphertext
    ciphertext = encryptMessage(myKey, myMessage)

    # Step 3: Print the encrypted string, with a pipe character at the end
    print(ciphertext + '|')

    # Step 4: Copy the encrypted string to the clipboard for easy access
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    # Step 1: Create a list to hold each column of the ciphertext
    ciphertext = [''] * key

    # Step 2: Loop through each column in ciphertext
    for col in range(key):
        pointer = col  # Start with the first character in the column

        # Step 3: Loop until the pointer goes past the length of the message
        while pointer < len(message):
            # Add the character at the current pointer to the corresponding column
            ciphertext[col] += message[pointer]
            # Move pointer down to the next row in the column
            pointer += key

    # Step 4: Convert the ciphertext list into a single string and return it
    return ''.join(ciphertext)

# Step 5: If this script is run directly, call the main() function
if __name__ == '__main__':
    main()
