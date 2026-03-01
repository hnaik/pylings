# Exercise: loops2
# Topic: Loops with range()
#
# range(n) creates the numbers 0, 1, 2, ... n-1
# range(start, stop) creates numbers from start up to (not including) stop
#
# Fix the loop to print the numbers 1 through 5.
#
# Hint: range(1, 6) gives you 1, 2, 3, 4, 5


def main():
    print("Counting from 1 to 5:")
    for i in range(???):
        print(i)

    # Now calculate the sum of 1 through 10
    total = 0
    for i in range(1, 11):
        total = total + i

    assert total == 55, f"Sum should be 55 but got {total}"
    print(f"Sum of 1 to 10 is: {total}")

if __name__ == "__main__":
    main()
