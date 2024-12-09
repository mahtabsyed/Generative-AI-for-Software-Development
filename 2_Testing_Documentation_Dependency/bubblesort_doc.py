# Prompt: Can you add docstring and inline doc for this function intended for an experienced develeoper
# Bubble sort algorithm
def bubbleSort(arr):
    """
    Sorts an array of numbers in ascending order using the bubble sort algorithm.

    Args:
        arr (list): A list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.

    The function works by repeatedly stepping through the list, comparing adjacent elements and swapping them if they are in the wrong order. This process is repeated until the list is sorted.
    """
    # Last i elements are already in place
    # Swap if the element found is greater than the next element
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Prompt: And now can you call this function with a list of 30 numbers
# Example usage of bubbleSort function
if __name__ == "__main__":
    # List of 30 numbers
    numbers = [ 64, 34, 25, 12, 22, 11, 90, 88, 76, 45, 33, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 2, 4, 6, 8, 10, 14, 16, 18, ]
    sorted_numbers = bubbleSort(numbers)
    print("Sorted list:", sorted_numbers)
