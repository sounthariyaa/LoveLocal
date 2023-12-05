# LoveLocal Assignment of Sounthariyaa J - ENG20AM0055
## EASY1 
## length_of_last_word Function

The `length_of_last_word` function takes a string as input and returns the length of the last word in the string. It follows a simple algorithm that involves iterating through the string from right to left, skipping trailing spaces, and counting the length of the last word.

## Function Explanation:

1. **Initialize Variables:**
   - `length`: To store the length of the last word.
   - `i`: Initialized to the last index of the string (`len(s) - 1`), starting from the end of the string.

2. **Skip Trailing Spaces:**
   - A `while` loop is used to skip any trailing spaces at the end of the string by moving backward until a non-space character is found.

3. **Count the Length of the Last Word:**
   - Another `while` loop is used to count the length of the last word by moving backward through the string until a space character is encountered.
   - The length is incremented for each non-space character.

4. **Return the Length:**
   - The function returns the calculated length of the last word.

## Example Usage:

```python
from typing import List

def length_of_last_word(s: str) -> int:
    # Initialize variables
    length = 0  # To store the length of the last word
    i = len(s) - 1  # Start from the last index of the string

    # Step 1: Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1  # Move backward through the string until a non-space character is found

    # Step 2: Count the length of the last word
    while i >= 0 and s[i] != ' ':
        length += 1  # Increment the length for each non-space character
        i -= 1  # Move backward through the string

    # Step 3: Return the length of the last word
    return length

# Example Usage:
# Take user input
user_input = input("Enter a string: ")

# Call the function and display the result
result = length_of_last_word(user_input)
print(f"The length of the last word is: {result}")
```

## Example Output:

For input `"Hello World"`, the output would be:
```
The length of the last word is: 5
```

## Time Complexity:
The time complexity of the function is O(n), where n is the length of the input string. The function iterates through the string once, performing constant-time operations at each step. This linear time complexity makes the function efficient for strings of varying lengths.


