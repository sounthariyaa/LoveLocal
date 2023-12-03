def length_of_last_word(s):
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

# Take user input
user_input = input("Enter a string: ")

# Call the function and display the result
result = length_of_last_word(user_input)
print(f"The length of the last word is: {result}")

#Time complexity of O(n) - counts the length in a linear fashion 
