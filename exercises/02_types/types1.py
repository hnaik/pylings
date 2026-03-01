# Exercise: types1
# Topic: Python Types - int and float
#
# Python has different types of values:
#   int   = whole numbers like 5, 100, -3
#   float = decimal numbers like 3.14, 0.5
#   str   = text like "hello"
#   bool  = True or False
#
# Fix the code so the assertions pass.
#
# Hint: Replace ??? with the right values. age should be a whole number.

# I AM NOT DONE

def main():
    age = ???
    height = ???
    name = ???
    is_student = ???

    assert isinstance(age, int), "age should be a whole number (int)"
    assert isinstance(height, float), "height should be a decimal number (float)"
    assert isinstance(name, str), "name should be text (str)"
    assert isinstance(is_student, bool), "is_student should be True or False (bool)"

    print(f"Name: {name}, Age: {age}, Height: {height}m, Student: {is_student}")
    print("Great job! You know your types!")

if __name__ == "__main__":
    main()
