# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator


def calculate_sum(numbers):
    """Return the sum of a list of numbers without using sum()."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Return the average of a list of numbers."""
    total = calculate_sum(numbers)
    return total / len(numbers)


def find_max(numbers):
    """Return the maximum value in a list without using max()."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def find_min(numbers):
    """Return the minimum value in a list without using min()."""
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


def main():
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    numbers = []
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = find_max(numbers)
    minimum = find_min(numbers)

    print("\nResults:")
    print(f"Sum:     {total:g}")
    print(f"Average: {average:g}")
    print(f"Maximum: {maximum:g}")
    print(f"Minimum: {minimum:g}")


if __name__ == "__main__":
    main()
