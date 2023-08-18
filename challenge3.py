def solve(s):
    consonant_values = {'a': 0, 'b': 2, 'c': 3, 'd': 4, 'e': 0,
                        'f': 6, 'g': 7, 'h': 8, 'i': 0, 'j': 10,
                        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 0,
                        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
                        'u': 0, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    def get_consonant_value(substring):
        value = 0
        for char in substring:
            value += consonant_values[char]
        return value

    max_value = 0
    current_substring = ""

    for char in s:
        if char in consonant_values:
            current_substring += char
        else:
            if current_substring:
                substring_value = get_consonant_value(current_substring)
                if substring_value > max_value:
                    max_value = substring_value
                current_substring = ""

    if current_substring:
        substring_value = get_consonant_value(current_substring)
        if substring_value > max_value:
            max_value = substring_value

    return max_value

print(solve("zodiacs"))
print(solve("strength")) 
