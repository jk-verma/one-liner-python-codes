'''
Problem    : COMPACT PHONE NUMBER FORMATTER
Description: The format_phone_number function offers a concise function to format an array of 10
             numbers into a phone number string in the standard (XXX) XXX-XXXX format.
@Author    : Dr. J. K. Verma
@Date      : 2025-09-20
'''


def format_phone_number(numbers):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)
numbers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
print(format_phone_number(numbers))
# Output: (555) 555-5555