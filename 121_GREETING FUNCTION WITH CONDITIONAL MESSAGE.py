'''
Problem    : GREETING FUNCTION WITH CONDITIONAL MESSAGE
Description: The say_hello_bye function introduces a one-liner function that takes a string name
             and a number (either 0 or 1) as input. Depending on the value of the number,
             it either greets the person with "Hello" or bids farewell with "Bye", while ensuring
             the name's first letter is capitalized. The function utilizes a ternary conditional
             operator for succinctness and clarity.
@Author    : Dr. J. K. Verma
@Date      : 2025-09-20
'''


def say_hello_bye(name, num):
    return f"Hello {name.capitalize()}" if num == 1 \
        else f"Bye {name.capitalize()}"
name = "Alice"
num = 2
print(say_hello_bye(name, num))
# Output: Bye Alice