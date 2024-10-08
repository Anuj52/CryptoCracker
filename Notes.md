# Writing the provided text to a .md file

text_content = """# Python Functions and Reverse Cipher Program

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
"""
