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

## EASY 3

## PASCAL's TRIANGLE

The `generate` method in the `Solution` class generates Pascal's Triangle up to a specified number of rows (`numRows`). The method follows an algorithm that efficiently constructs each row of the triangle based on the values of the previous row.

## Method Explanation:

1. **Initialize Triangle:**
   - The `triangle` list is initialized to store the rows of Pascal's Triangle.

2. **Base Case for the First Row:**
   - If `numRows` is greater than or equal to 1, the base case for the first row `[1]` is added to the `triangle`.

3. **Loop to Generate Subsequent Rows:**
   - A `for` loop iterates from the second row (`row_num = 1`) up to the specified number of rows (`numRows`).
   - Each row is initialized with the first element as 1 (`row = [1]`).

4. **Optimize the Inner Loop:**
   - An inner `for` loop iterates through the row, skipping the first and last elements.
   - The inner loop efficiently calculates each element in the row by summing the corresponding elements from the previous row.

5. **Add the Last Element:**
   - The last element of each row is always 1, so it is appended to the row.

6. **Add the Row to Triangle:**
   - The generated row is appended to the `triangle` list.

7. **Return Triangle:**
   - The method returns the complete Pascal's Triangle stored in the `triangle` list.

## Example Usage:

```python
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        # Base case for the first row
        if numRows >= 1:
            triangle.append([1])

        # Loop to generate subsequent rows
        for row_num in range(1, numRows):
            row = [1]  # Initialize row with the first element as 1

            # Optimize the inner loop
            for i in range(1, row_num):
                row.append(triangle[row_num - 1][i - 1] + triangle[row_num - 1][i])

            # The last element of each row is always 1
            row.append(1)

            triangle.append(row)

        return triangle

# Example usage
numRows = 5
result = Solution().generate(numRows)
print(result)
```

### Example Output:

For `numRows = 5`, the output would be:
```
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

### Time Complexity:
The time complexity of the `generate` method is O(numRows^2), where `numRows` is the number of rows in Pascal's Triangle. The method efficiently constructs each row, performing constant-time operations at each step.

## MEDIUM2

# majorityElement Method in Solution Class

The `majorityElement` method in the `Solution` class identifies elements that appear more than ⌊ n/3 ⌋ times in a given list of integers (`nums`). It uses a Counter to efficiently count the occurrences of each element and then iterates through the counts to find majority elements.

## Method Explanation:

1. **Create Counter:**
   - The method creates a Counter (`element_count`) to store the count of each element in the input list (`nums`).

2. **Identify Majority Elements:**
   - A list (`majority_elements`) is initialized to store the identified majority elements.
   - A threshold is calculated as ⌊ n/3 ⌋, where `n` is the length of the input list.
   - The method iterates through the element count to identify elements with counts greater than the threshold, and appends them to `majority_elements`.

3. **Return Majority Elements:**
   - The method returns the list of majority elements.

## Example Usage:

```python
from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # Create a Counter to store the count of each element
        element_count = Counter(nums)
        
        majority_elements = []
        threshold = len(nums) // 3
        
        # Iterate through the element count to identify majority elements
        for element, count in element_count.items():
            # Check if the element count is greater than the threshold
            if count > threshold:
                majority_elements.append(element)
        
        return majority_elements

# Example usage
# Take user input for a list of integers
user_input = input("Enter a list of integers separated by spaces: ")
nums = list(map(int, user_input.split()))

# Create an instance of the Solution class
solution = Solution()

# Call the majorityElement method and print the result
result = solution.majorityElement(nums)
print("Majority Elements:", result)
```

## Example Output:

For input `nums = [3, 3, 2, 2, 2, 4, 4, 4]`, the output would be:
```
Majority Elements: [2, 4]
```

## Time Complexity:
The time complexity of the `majorityElement` method is O(n), where n is the length of the input list. The method efficiently counts the occurrences of each element using a Counter and iterates through the counts, performing constant-time operations at each step.


#HARD2

##ShortestPalindrome Function

The `shortestPalindrome` function converts a given string to its shortest palindrome by adding characters in front of the string. It follows an algorithm that iteratively checks substrings and adds characters until a palindrome is formed.

## Function Explanation:

1. **Get User Input:**
   - The function prompts the user to enter a string.

2. **Reverse the String:**
   - The original string is reversed to create a reversed version (`p`).

3. **Initialize Variables:**
   - `add`: A string initialized to hold added characters.
   - `n`: The length of the original string.

4. **Iterate Through Positions:**
   - A `for` loop iterates through positions in the original string.
   - Substrings `a` and `b` are extracted based on the current position.

5. **Check Substring Equality:**
   - The function checks if substrings `a` and `b` are equal.
   - If not equal, the last character of `a` is added to `add`.
   - If equal, the loop is terminated.

6. **Combine and Return:**
   - The shortest palindrome is formed by combining `add` and the original string (`s`).
   - The function prints and returns the shortest palindrome.

## Example Usage:

```python
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
```

## Example Output:

For input `"abcd"`, the output would be:
```
Shortest palindrome: "dcbabcd"
```

## Time Complexity:
The overall time complexity of the function is O(n), where n is the length of the input string `s`. The function iterates through the string once, performing constant-time operations at each step.
