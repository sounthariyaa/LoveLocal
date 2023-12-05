def majorityElement(nums):
  """
  Finds all elements that appear more than ⌊ n/3 ⌋ times in an integer array.

  Args:
      nums: An integer array.

  Returns:
      A list of elements that appear more than ⌊ n/3 ⌋ times.
  """
  threshold = len(nums) // 3
  candidates = set()
  element_counts = defaultdict(int)
  for num in nums:
    element_counts[num] += 1
    if element_counts[num] > threshold:
      candidates.add(num)
  
  # Filter candidates by verifying their actual counts
  for num in candidates:
    if element_counts[num] <= threshold:
      candidates.remove(num)

  return list(candidates)

# Get user input
nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))

# Find and print the majority elements
result = majorityElement(nums)
print(f"Elements appearing more than ⌊ n/3 ⌋ times: {result}")
