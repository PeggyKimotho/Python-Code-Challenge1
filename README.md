# Python-Code-Challenge1

## Challenge1: Converting 12-hour time to 24-hour time

I started with writing the convert_to_24_hour function.

This function takes three arguments: hour, minute, and period. 

It begins by checking if the given period is "am" or "pm".

If it's "am" and the hour is 12, the hour is set to 0, representing midnight.

If it's "pm" and the hour is not 12, 12 hours are added to the hour to convert to 24-hour format.

The function then formats the hour and minute as a four-digit string and returns the result.

This converts a 12-hour time representation to a 24-hour format.


## Challenge 2: Two numbers are positive

I started with writing the two_positive_numbers function.

This function takes three integer arguments: a, b, and c. 

The function initializes a positive_number_count variable to keep track of the number of positive integers.

It checks each integer (a, b, and c) to see if it is positive (greater than 0) and increments positive_number_count accordingly.

It then determines whether exactly two out of the three integers are positive.

## Challenge 3: Consonant value

I started by writing the solve function.

It takes a lowercase string (s).

The function defines a consonant_values dictionary containing all the characters.

A nested get_consonant_value function then calculates the value of a consonant substring using the consonant_values dictionary.

The main function iterates through the input string, identifying consonant substrings and calculating their values.

It calculates the highest value of consonant substrings, where consonants are any letters of the alphabet except "aeiou."

