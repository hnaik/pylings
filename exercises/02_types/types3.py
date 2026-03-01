# Exercise: types3
# Topic: The type() Function
#
# The type() function tells you what type a value is.
# type(42)     gives <class 'int'>
# type("hi")   gives <class 'str'>
# type(3.14)   gives <class 'float'>
# type(True)   gives <class 'bool'>
#
# Fix the code so it prints the correct types.
#
# Hint: Use type() and compare with int, str, float, or bool.

# I AM NOT DONE

def main():
    my_number = 100
    my_text = "Python"
    my_decimal = 2.718
    my_bool = False

    assert type(my_number) == ???, "What type is 100?"
    assert type(my_text) == ???, "What type is 'Python'?"
    assert type(my_decimal) == ???, "What type is 2.718?"
    assert type(my_bool) == ???, "What type is False?"

    print("You know your types! 🎉")

if __name__ == "__main__":
    main()
