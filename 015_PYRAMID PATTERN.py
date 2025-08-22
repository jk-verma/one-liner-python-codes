'''
Problem    : PYRAMID PATTERN
Description: The create_pyramid function takes the number of rows as an argument and
             returns an array representing the pyramid pattern.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''

def create_pyramid(rows):
    return [f"{' ' * (rows - i)}{'*' * (2 * i - 1)}" for i in range(1, rows + 1)]

pyramid = create_pyramid(5)
for row in pyramid: print(row)

"""
            *
           ***
          *****
         *******
        *********
"""