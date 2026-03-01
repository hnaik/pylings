# Exercise: errors2
# Topic: Catching Different Errors
#
# Different things can go wrong! You can catch different error types.
# ValueError happens when you try to convert invalid data.
#
# Fix the function to return None if the conversion fails.
#
# Hint:
# try:
#     return int(text)
# except ValueError:
#     return None


def safe_int(text):
    ???

def main():
    assert safe_int("42") == 42, "Should convert '42' to 42"
    assert safe_int("hello") is None, "Should return None for 'hello'"
    assert safe_int("") is None, "Should return None for empty string"
    assert safe_int("100") == 100, "Should convert '100' to 100"

    print(f"'42' -> {safe_int('42')}")
    print(f"'hello' -> {safe_int('hello')}")
    print(f"'' -> {safe_int('')}")
    print("ValueError handling works!")

if __name__ == "__main__":
    main()
