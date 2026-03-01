# Exercise: strings3
# Topic: String Methods
#
# Strings come with built-in tools called methods.
# .upper() -> makes ALL CAPS
# .lower() -> makes all lowercase
# .split() -> splits into a list of words
# .strip() -> removes spaces from the start and end
#
# Fix the assertions below.
#
# Hint: call the method on the string like: my_string.upper()


def main():
    greeting = "hello, world!"
    loud = ???    # Should be "HELLO, WORLD!"

    message = "  Python is fun!  "
    clean = ???   # Should be "Python is fun!" (no extra spaces)

    sentence = "I love coding"
    words = ???   # Should be ["I", "love", "coding"]

    assert loud == "HELLO, WORLD!", f"Got: {loud}"
    assert clean == "Python is fun!", f"Got: '{clean}'"
    assert words == ["I", "love", "coding"], f"Got: {words}"

    print("String methods work great!")

if __name__ == "__main__":
    main()
