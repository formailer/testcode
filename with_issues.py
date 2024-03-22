def calculate_average(numbers):
  """Calculates the average of a list of numbers.

  Args:
      numbers: A list of numbers.

  Returns:
      The average of the numbers, or None if the list is empty.

  Raises:
      TypeError: If any element in the list is not a number.
  """

  # Bug 1: Incorrect handling of empty lists (should return 0)
  if not numbers:
    return None

  # Bug 2: Integer division for non-integers (should use float division)
  total = sum(numbers)
  average = total / len(numbers)

  return average

def is_prime(number):
  """Checks if a number is prime.

  Args:
      number: A positive integer.

  Returns:
      True if the number is prime, False otherwise.

  Raises:
      ValueError: If the number is not positive.
  """

  # Bug 3: Inefficient primality check (use trial division for better performance)
  if number <= 1:
    raise ValueError("Number must be positive")
  if number <= 3:
    return True

  # Only check for divisibility up to the square root of the number (optimization)
  for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
      return False
  return True

def find_largest_word(words):
  """Finds the largest word in a list of words.

  Args:
      words: A list of strings.

  Returns:
      The largest word in the list, or None if the list is empty.

  Raises:
      TypeError: If any element in the list is not a string.
  """

  # Bug 4: No handling for non-strings in the list (should raise TypeError)
  if not words:
    return None

  largest_word = words[0]
  for word in words[1:]:
    if len(word) > len(largest_word):
      largest_word = word

  return largest_word
