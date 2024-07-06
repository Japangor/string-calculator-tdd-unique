import re

def add(numbers):
    if not numbers:
        return 0

    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)
    else:
        delimiter = ",|\n"
    
    parts = re.split(delimiter, numbers)
    
    total = 0
    negatives = []

    for part in parts:
        num = int(part)
        if num < 0:
            negatives.append(num)
        total += num

    if negatives:
        raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")

    return total
