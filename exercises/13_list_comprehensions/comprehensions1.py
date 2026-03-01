# Exercise: comprehensions1
# Topic: List Comprehensions
#
# A list comprehension creates a new list in one short line!
# Instead of a loop, you can write: [expression for item in list]
#
# Fix the code to use list comprehensions.
#
# Hint: [n * 2 for n in numbers] creates a list of doubled numbers

# I AM NOT DONE

def main():
    numbers = [1, 2, 3, 4, 5]

    # Create a list of doubled numbers using a list comprehension
    doubled = ???

    assert doubled == [2, 4, 6, 8, 10], f"Got: {doubled}"

    # Create a list of squares (n * n) for each number
    squares = ???

    assert squares == [1, 4, 9, 16, 25], f"Got: {squares}"

    print(f"Numbers: {numbers}")
    print(f"Doubled: {doubled}")
    print(f"Squares: {squares}")
    print("List comprehensions are so cool!")

if __name__ == "__main__":
    main()
