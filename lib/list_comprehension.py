#!/usr/bin/env python3

def return_evens(numbers):
    return [num for num in numbers if num % 2 == 0]

# Example usage
print(return_evens([0, 1, 3, 5, 7, 8, 9]))  
# Output: [0, 8]

def make_exclamation(sentences):
    return [sentence + "!" for sentence in sentences]
