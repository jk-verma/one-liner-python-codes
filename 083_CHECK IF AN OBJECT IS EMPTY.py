# CHECK IF AN OBJECT IS EMPTY

# The IsEmptyObject function checks if a given object has no own properties.

def IsEmptyObject(obj):
    return len(obj) == 0
# Example usage
print(IsEmptyObject({})) # Output: True
print(IsEmptyObject({"name": "John", "age": 30}))
# Output: False