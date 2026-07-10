def dummy_divide (a, b):
    if b==0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

print(dummy_divide(115, 2))