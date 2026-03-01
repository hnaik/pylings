# Exercise: comprehensions2
# Topic: Filtering with List Comprehensions
#
# You can add an `if` condition to a list comprehension to filter items!
# [item for item in list if condition]
#
# Fix the code to use filtering comprehensions.
#
# Hint: [n for n in numbers if n % 2 == 0] keeps only even numbers

# I AM NOT DONE

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Get only the even numbers
    evens = ???

    assert evens == [2, 4, 6, 8, 10], f"Got: {evens}"

    # Get only numbers greater than 5
    big_numbers = ???

    assert big_numbers == [6, 7, 8, 9, 10], f"Got: {big_numbers}"

    print(f"All numbers: {numbers}")
    print(f"Even numbers: {evens}")
    print(f"Numbers > 5: {big_numbers}")
    print("Filtering comprehensions work!")

if __name__ == "__main__":
    main()
