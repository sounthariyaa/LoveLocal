def generate(numRows):
  """
  Generates the first numRows of Pascal's triangle.

  Args:
      numRows: An integer representing the desired number of rows.

  Returns:
      A list of lists representing the first numRows of Pascal's triangle.
  """
  triangle = []

  # Base case for the first row
  if numRows >= 1:
    triangle.append([1])

  # Loop to generate subsequent rows
  for row_num in range(1, numRows):
    row = [1] * (row_num + 1)  # Initialize row with 1s

    # compute each element using previous row
    for i in range(1, row_num):
      row[i] = triangle[row_num - 1][i - 1] + triangle[row_num - 1][i]

    triangle.append(row)

  return triangle

numRows = int(input("Enter the number of rows: "))
triangle = generate(numRows)
for row in triangle:
  print(row)

#The time complexity of the code is O(n^2), where n is the number of rows in Pascal's triangle. This is because the outer loop iterates through n rows, and the inner loop iterates through the elements of each row, which takes n time per iteration.