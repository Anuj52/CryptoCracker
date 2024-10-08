# Python Functions and Reverse Cipher Program

# ---- Notes ----
"""
Functions:
A function is kind of like a mini-program inside your program. It contains lines of code that are
executed from top to bottom. Python provides some built-in functions that we can use (you’ve
already used the print() function). The great thing about functions is that we only need to 
know what the function does, but not how it does it.
"""

"""
A function call is a piece of code that tells our program to run the code inside a function.
For example, your program can call the print() function whenever you want to display a string
on the screen.
"""

# ---- Example of a Function Call ----
print('Hello world!')
print('What is your name?')

# The input() function
"""
The input() function allows the user to enter data. Once the program executes the input line,
it waits for the user to provide some input. The data provided is stored in a variable.
"""

myName = input()  # Stores the input from the user in the variable myName

"""
Once the program executes the last line, it stops. At this point, it has terminated or exited,
and all of the variables are forgotten by the computer, including the string we stored in myName.
If you try running the program again and typing a different name, it will print that name.
"""

# ---- The Reverse Cipher ----
"""
The reverse cipher encrypts a message by printing it in reverse order. For example, “Hello world!”
encrypts to “!dlrow olleH”. To decrypt, you simply reverse the reversed message to get the original
message. The encryption and decryption steps are the same.
The reverse cipher is a very weak cipher. Just by looking at its ciphertext, you can figure out that
it's just in reverse order.
"""

# ---- Reverse Cipher Code ----
message = 'Three can keep a secret, if two of them are dead.'
translated = ''  # This will hold the reversed message
i = len(message) - 1  # Initialize the index i to the last character of the message

while i >= 0:  # Loop through the message in reverse order
    translated = translated + message[i]  # Add each character to the translated string
    i = i - 1  # Move to the previous character

print(translated)  # Print the reversed message


# reverseCipher.py - Introduction to the while Loop

# ---- Notes ----
"""
Introducing the while Loop:
A while loop is a new type of Python instruction. It repeats a block of code as long as a condition is True. 
The while loop is made up of four parts:

1. The while keyword.
2. An expression (also called a condition) that evaluates to the Boolean values True or False.
3. A : colon.
4. A block of indented code that comes after it, which is what lines 9 and 10 are.
"""

# ---- Reverse Cipher Code with a while Loop ----
message = 'Three can keep a secret, if two of them are dead.'
translated = ''  # This will hold the reversed message
i = len(message) - 1  # Initialize the index i to the last character of the message

# 8. while i >= 0:
# This while loop keeps running as long as the condition i >= 0 is True. When i becomes negative, the loop stops.
while i >= 0:  # Loop through the message in reverse order
    translated = translated + message[i]  # Add each character to the translated string
    i = i - 1  # Decrease the index i by 1 in each iteration, moving to the previous character

print(translated)  # Print the reversed message

# ---- Explanation of the while Loop ----
"""
Explanation of the while Loop:
- The while keyword begins the loop.
- The expression i >= 0 is checked before each iteration. If it evaluates to True, the loop runs. If it evaluates to False, the loop ends.
- The colon (:) indicates that the indented block of code that follows is part of the loop.
- The block of indented code (lines 9 and 10) repeats while the condition is True.

In this case, the while loop starts with i set to the last index of the string and continues to loop until i is less than 0, 
meaning it has processed every character in the string in reverse order.
"""
# reverseCipher.py - Short Explanation of Boolean, Comparison Operators, and while Loop

# The Boolean Data Type:
# Booleans have two values: True or False. They're case-sensitive (capitalize T and F).

# Comparison Operators:
# <, >, <=, >=, ==, != are used to compare values and return a Boolean result.

# Example:
# >>> 0 < 6       # True
# >>> 10 < 10     # False

# Blocks: 
# A block is indented code. The while loop below has two lines (9, 10) inside its block.

# ---- Reverse Cipher Code ----

message = 'Three can keep a secret, if two of them are dead.'
translated = ''
i = len(message) - 1  # Set i to the last character index

while i >= 0:  # The loop continues until i is less than 0
    translated = translated + message[i]  # Add each character in reverse
    print(i, message[i], translated)  # Observe how translated grows
    i = i - 1  # Decrease i by 1

print(translated)  # Final reversed message

# Sample Output: '.daed era meht fo owt fi ,terces a peek nac eerhT'



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


# This function encrypts a message using the Caesar cipher
def caesar_cipher(message, key):
    # Initialize the translated message
    translated = ''

"""
This function encrypts a message using the Caesar cipher.
It shifts each letter by a specified key.
Parameters:
- message (str): The message to be encrypted.
- key (int): The number of positions to shift each letter.
Returns:
- str: The encrypted message.
def caesar_cipher(message, key):
"""



def caesar_cipher(message: str, key: int) -> str:
    """
    Encrypts a message using the Caesar cipher algorithm.
    
    Parameters:
    - message (str): The message to encrypt.
    - key (int): The shift value for encryption.

    Returns:
    - str: The encrypted message.
    """
    translated = ''
    # Loop through each character in the message
    for symbol in message:
        # (Encryption logic goes here)
        return translated

# --- Imports ---
import pyperclip  # For copying the result to clipboard

# --- Constants ---
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# --- Functions ---
def caesar_cipher(message: str, key: int) -> str:
    """Encrypts a message using the Caesar cipher."""
    # (Function code here)

# --- Main Program ---
if __name__ == '__main__':
    # Get user input
    message = input("Enter the message: ")
    key = int(input("Enter the shift key: "))
    
    # Encrypt the message
    encrypted_message = caesar_cipher(message, key)
    print(f'Encrypted Message: {encrypted_message}')

def caesar_cipher(message: str, key: int) -> str:
    translated = ''
    
    for symbol in message:
        if symbol.isalpha():  # Check if the symbol is a letter
            # Shift the letter and wrap around the alphabet
            shifted_index = (ALPHABET.index(symbol.upper()) + key) % 26
            translated += ALPHABET[shifted_index]  # Append the translated letter
        else:
            translated += symbol  # Non-letter characters are unchanged
    return translated


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

'''The critical failure of the Caesar cipher is that there aren’t that many different possible keys that 
can be used to encrypt a message. Any computer can easily decrypt with all 26 possible keys, and 
it only takes the cryptanalyst a few seconds to look through them to find the one that is in 
English. To make our messages more secure, we will need a cipher that has more possible keys. 
That transposition cipher in the next chapter can provide this for us.'''

'''Key Concepts from the Chapter
Transposition Cipher vs. Caesar Cipher:

The Transposition Cipher is more complex and secure than the Caesar Cipher. While the Caesar Cipher shifts letters, the Transposition Cipher rearranges them, making it harder to decipher without the key.
Functions:

Functions are defined using the def statement, allowing you to encapsulate code for reuse. This helps in organizing the code into logical sections, improving readability and maintainability.
Arguments can be passed to functions, allowing you to customize their behavior based on input.
Local and Global Variables:

Local Variables: Defined within functions and only accessible there. They can have the same name as global variables without conflict.
Global Variables: Defined outside of all functions and accessible throughout the program. Care should be taken to avoid naming conflicts.
Lists:

Lists can hold multiple values, including other lists (nested lists). They are versatile data structures in Python.
You can perform operations on lists similar to those on strings, such as indexing, slicing, and using the len() function to determine their length.
Augmented Assignment Operators:

These operators provide a shorthand for updating variables (e.g., x += 1 is equivalent to x = x + 1). They make the code more concise and easier to read.
String Manipulation:

The join() method is a powerful way to combine elements of a list into a single string, especially when you need to insert a specific separator (like commas or spaces) between elements.
Additional Notes
Step-by-Step Evaluation: Understanding how Python evaluates code line by line is crucial. This means tracing through your code and observing how data is manipulated at each step.

Practice and Reinforcement: Revisiting these concepts through coding exercises or small projects will solidify your understanding. Implementing both the encryption and decryption of the Transposition Cipher would be a great way to apply what you've learned.

Next Steps
As you move to the next chapter, which focuses on decrypting with the transposition cipher, consider the following:

Revisit the Encryption Process: Make sure you understand how the encryption function works. This will help you understand the decryption process, as they are closely related.

Implement Decryption: Try to implement the decryption process yourself based on the encryption logic. This will deepen your understanding of how transposition ciphers operate.

Experiment with Variations: Modify the key or message and observe how the outputs change. This will give you hands-on experience with the concepts discussed.'''

# Transposition Cipher Decryption

import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)

    # Print with a | (called "pipe" character) after it in case
    # there are spaces at the end of the decrypted message.
    print(plaintext + '|')

    # Copy the decrypted string to the clipboard.
    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    numOfColumns = math.ceil(len(message) / key)
    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns

    # The col and row variables point to where in the grid the next
    # character in the encrypted message will go.
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1  # point to next column

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row.
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)

# If transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
'''Explanation of the Code
Imports:

math: Used to perform mathematical operations, specifically to calculate the number of columns in the transposition grid.
pyperclip: This module allows copying the decrypted text to the clipboard.
Main Function:

Initializes myMessage with the encrypted message and myKey with the key used for encryption.
Calls the decryptMessage function to decrypt the message.
Prints the decrypted message with a pipe character (|) at the end to indicate any trailing spaces.
Copies the decrypted message to the clipboard.
Decrypt Function (decryptMessage):

Calculates the number of columns in the grid by taking the ceiling of the length of the message divided by the key.
Sets the number of rows to the key value.
Determines the number of shaded boxes (unused spaces) in the last column.
Initializes a list, plaintext, to hold the characters of each column.
Loops through each character in the encrypted message, placing them into the appropriate column in the plaintext list.
Checks if it needs to reset the column index and move to the next row based on the number of columns and shaded boxes.
Returns the joined string of the plaintext list, which is the decrypted message.
Execution Check:

The if __name__ == '__main__': block ensures that main() is called only when the script is run directly, not when it is imported as a module'''


# Transposition Cipher Test
# http://inventwithpython.com/hacking (BSD Licensed)

import random
import sys
import transpositionEncrypt
import transpositionDecrypt

def main():
    random.seed(42)  # Set the random "seed" to a static value

    for i in range(20):  # Run 20 tests
        # Generate random messages to test.
        
        # The message will have a random length:
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # Convert the message string to a list to shuffle it.
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)  # Convert list to string

        print('Test #%s: "%s..."' % (i + 1, message[:50]))  # Show the first 50 characters

        # Check all possible keys for each message.
        for key in range(1, len(message)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            # If the decryption doesn't match the original message, display
            # an error message and quit.
            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print(decrypted)
                sys.exit()

    print('Transposition cipher test passed.')

# If transpositionTest.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()


'''Imports:

The program imports the random module for generating random messages, the sys module for system exit functionality, and the custom modules transpositionEncrypt and transpositionDecrypt for encryption and decryption functions.
Main Function:

The main() function generates and tests random messages to ensure that the encryption and decryption processes work correctly.
Random Seed:

random.seed(42) sets a static seed for random number generation, ensuring that the same sequence of random values is generated each time the program runs.
Test Loop:

The outer loop (for i in range(20)) runs the test 20 times.
Each iteration generates a random message by multiplying a string of letters ('ABCDEFGHIJKLMNOPQRSTUVWXYZ') by a random integer between 4 and 40, creating a message of random length.
Shuffling:

The message is converted to a list and shuffled to create a random order of characters.
The shuffled list is then converted back to a string.
Key Testing:

The inner loop iterates over all possible keys (from 1 to the length of the message) and encrypts the message using the current key.
It then decrypts the encrypted message using the same key.
Mismatch Check:

If the decrypted message does not match the original message, an error message is printed, and the program exits using sys.exit().
The error message displays the key used and the mismatched message.
Success Message:

If all tests pass without mismatches, it prints "Transposition cipher test passed."'''


'''_______________________________________________________________________________________________________________________________'''


'''Key Concepts in Ciphers
Brute-Force Attack: A method of cracking a cipher by systematically trying every possible key until the correct one is found.

Caesar Cipher: A substitution cipher that shifts letters in the alphabet. The example provided shows how to create a program to hack the Caesar cipher using brute-force.

Transposition Cipher: Instead of replacing characters, this method rearranges the characters in a specific order. You learned to encrypt and decrypt messages using a grid method based on a key.

Functions: The use of functions (def) helps organize code, and parameters are used to pass values to these functions. Understanding the distinction between local and global variables is crucial.

List Manipulation: Lists can store multiple values, and methods like join() are used to convert lists back to strings.

Randomization: The random module is utilized for generating random messages and keys for testing, although it's noted that these pseudorandom numbers are not suitable for cryptography.

Testing Programs
Automated Testing: Writing a separate test program to validate that the encryption and decryption functions work correctly for a variety of inputs ensures reliability.

Error Handling: The test program checks for mismatches between the original and decrypted messages and exits if discrepancies are found.

Deep Copying: Understanding the difference between reference values and deep copies is essential for working with lists and other mutable data types.'''
