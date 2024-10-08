# caesarHacker.py

# Caesar Cipher Hacker
# This program decrypts a Caesar cipher by attempting every possible key.


# Encrypted message to be decrypted
message = 'GUVF VF ZL FRPERG ZRFFNTR.'

# Constant defining the alphabet used in the cipher
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Loop through every possible key from 0 to 25 (total 26 letters)
for key in range(len(LETTERS)):
    
    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared.
    translated = ''
    
    # The rest of the program is the same as the original Caesar program:
    
    # Run the decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:  # Check if the symbol is a letter in the alphabet
            num = LETTERS.find(symbol)  # Get the index of the symbol
            num = num - key  # Decrypt the symbol by shifting it backward

            # Handle the wrap-around if num is less than 0
            if num < 0:
                num = num + len(LETTERS)  # Wrap around to the end of the alphabet

            # Add the decrypted symbol to the translated message
            translated = translated + LETTERS[num]
        else:
            # If the symbol is not in LETTERS, add it unchanged
            translated = translated + symbol
    
    # Display the current key being tested, along with its decryption
    print('Key #%s: %s' % (key, translated))  # Output the key and the decrypted message
