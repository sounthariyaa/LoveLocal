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
