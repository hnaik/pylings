# Exercise: types2
# Topic: Type Conversion
#
# Sometimes you need to convert between types.
# int("5") turns the text "5" into the number 5
# str(42) turns the number 42 into text "42"
# float("3.14") turns text into a decimal
#
# Fix the code so the assertions pass.
#
# Hint: Use int(), float(), or str() to convert the values.


def main():
    number_text = "42"
    number = ???  # Convert number_text to an integer

    price_text = "9.99"
    price = ???  # Convert price_text to a float

    count = 7
    count_text = ???  # Convert count to a string

    assert isinstance(number, int), "number should be an int"
    assert isinstance(price, float), "price should be a float"
    assert isinstance(count_text, str), "count_text should be a str"
    assert number == 42
    assert price == 9.99
    assert count_text == "7"

    print("Type conversion works!")

if __name__ == "__main__":
    main()
