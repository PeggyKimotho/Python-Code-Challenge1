# Python-Code-Challenge1

The convert_to_24_hour function takes three arguments: hour, minute, and period (am/pm). It converts a 12-hour time representation to a 24-hour format.

Explanation:

The function begins by checking if the given period is "am" or "pm".
If it's "am" and the hour is 12, the hour is set to 0, representing midnight.
If it's "pm" and the hour is not 12, 12 hours are added to the hour to convert to 24-hour format.
The function then formats the hour and minute as a four-digit string and returns the result.
