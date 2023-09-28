#!/usr/bin/env python3


def print_fibonacci(length):
    if length <= 0:
        print([]) 
        return
    elif length == 1:
        print([0])  
        return

    fib_sequence = [0, 1]

    while len(fib_sequence) < length:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    for number in fib_sequence:
        print(number)

# Example usage:
print_fibonacci(0)   # Prints []
print_fibonacci(1)   # Prints [0]
print_fibonacci(2)   # Prints [0, 1]
print_fibonacci(10)  # Prints [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

