# GENERATE MULTIPLICATION TABLE

# The GenerateMultiplicationTable function creates a multiplication table of a specified size.

def GenerateMultiplicationTable(size):
    table = [[(row + 1) * (col + 1) for col in range(size)] for
    row in range(size)]
    return table
# Example usage
size = 5
multiplicationTable = GenerateMultiplicationTable(size)
for row in multiplicationTable:
    print(", ".join(map(str, row)))