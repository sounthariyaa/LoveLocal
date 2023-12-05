def shortestPalindrome(): 
    # Get user input
    s = input("Enter the string to convert to a palindrome: ")

    p = s[::-1]  # Reverse the original string
    add = ""  # Initialize the string to hold added characters

    n = len(s)  # Store the string length

    # Iterate through positions in the original string
    for i in range(n):
        # Extract substrings
        a = s[0:n - i]  # From beginning excluding last i characters
        b = p[i:]  # From reversed string starting at position i

        # Check if substrings are equal
        if a != b:
            add += a[-1]  # Add last character of a if not equal
        else:
            break  # Stop the loop if equal

    # Combine and return the shortest palindrome
    shortest_palindrome = add + s
    print(f"Shortest palindrome: {shortest_palindrome}")
    return shortest_palindrome

# Run the function
shortestPalindrome()

#Overall time complexity of the function is O(n), where n is the length of the input string s.