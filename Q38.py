def add_numbers(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

# Example usage:
print("Sum:", add_numbers(5, 3))
