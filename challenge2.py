def two_positive_numbers(a, b, c):
    positive_number_count = 0
    
    if a > 0:
        positive_number_count += 1
    if b > 0:
        positive_number_count += 1
    if c > 0:
        positive_number_count += 1
    
    return positive_number_count == 2

print(two_positive_numbers(2, -4, 6))
print(two_positive_numbers(6, 8, 10))