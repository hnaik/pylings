# Exercise: errors3
# Topic: Raising Errors
#
# You can create your own errors with `raise`!
# This is useful when someone gives your function bad input.
#
# Fix the function to raise a ValueError when age is negative.
#
# Hint: raise ValueError("Age cannot be negative!")

# I AM NOT DONE

def validate_age(age):
    if age < 0:
        ???
    return age

def main():
    assert validate_age(25) == 25, "25 is a valid age"
    assert validate_age(0) == 0, "0 is a valid age"

    try:
        validate_age(-1)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        print(f"Caught expected error: {e}")

    print("Age validator works!")

if __name__ == "__main__":
    main()
