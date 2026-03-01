# Exercise: errors1
# Topic: Try and Except
#
# Errors happen! Instead of crashing, you can handle them gracefully.
# Use try/except to catch errors and do something about them.
#
# Fix the code so it catches the ZeroDivisionError and prints
# "Oops! Can't divide by zero!" instead of crashing.
#
# Hint:
# try:
#     risky_code()
# except ZeroDivisionError:
#     print("handle the error here")

# I AM NOT DONE

def safe_divide(a, b):
    ???

def main():
    result = safe_divide(10, 2)
    assert result == 5.0, f"Expected 5.0, got {result}"

    result2 = safe_divide(10, 0)
    assert result2 is None, f"Should return None for division by zero, got {result2}"

    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    print("Error handling works!")

if __name__ == "__main__":
    main()
