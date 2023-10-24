def insertion_sort(array):
  """Sorts an array using the insertion sort algorithm.

  Args:
    array: A list of elements to be sorted.

  Returns:
    A sorted list of elements.
  """

  # Iterate over the array starting from the second element.
  for i in range(1, len(array)):
    # Store the current element as the key.
    key = array[i]

    # Iterate over the sorted portion of the array, starting from the end.
    j = i - 1
    while j >= 0 and array[j] > key:
      # Shift the element to the right.
      array[j + 1] = array[j]

      # Decrement the index of the sorted portion of the array.
      j -= 1

    # Insert the key into the sorted portion of the array.
    array[j + 1] = key

  # Return the sorted array.
  return array


# Example usage:

array = [5, 3, 8, 6, 7, 2]

# Sort the array using the insertion sort algorithm.
sorted_array = insertion_sort(array)

# Print the sorted array.
print(sorted_array)
