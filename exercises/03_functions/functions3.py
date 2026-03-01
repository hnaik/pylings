# Exercise: functions3
# Topic: Functions that Return Values
#
# Functions can give back a result using `return`.
# The result can be saved in a variable.
#
# Fix the add function so it returns the sum of a and b.
#
# Hint: return a + b

# I AM NOT DONE

def add(a, b):
    ???

def main():
    result = add(3, 4)
    assert result == 7, f"Expected 7 but got {result}"

    result2 = add(10, 25)
    assert result2 == 35, f"Expected 35 but got {result2}"

    print(f"3 + 4 = {add(3, 4)}")
    print(f"10 + 25 = {add(10, 25)}")
    print("Your function works great!")

if __name__ == "__main__":
    main()
