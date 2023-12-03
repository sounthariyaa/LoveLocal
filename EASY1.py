def length_of_last_word(s):
    length = 0
    i = len(s) - 1

    # Skip empty spaces
    while i >= 0 and s[i] == ' ':
        i -= 1

    # Count the length of the last word
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length

# Take user input
user_input = input("Enter a string: ")

# Call the function and display the result
result = length_of_last_word(user_input)
print(f"The length of the last word is: {result}")
