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

# Take user input for a list of integers
user_input = input("Enter a list of integers separated by spaces: ")
nums = list(map(int, user_input.split()))

# Create an instance of the Solution class
solution = Solution()

# Call the majorityElement method and print the result
result = solution.majorityElement(nums)
print("Majority Elements:", result)
