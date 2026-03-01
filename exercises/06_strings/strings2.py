# Exercise: strings2
# Topic: F-strings
#
# F-strings let you put variables inside text easily!
# Put an f before the quotes, then use {} to include variables.
#
# name = "Alex"
# f"Hello, {name}!"  gives  "Hello, Alex!"
#
# Fix the code to build the message using an f-string.
#
# Hint: f"My name is {name} and I am {age} years old."

# I AM NOT DONE

def main():
    name = "Jordan"
    age = 14
    favorite_color = "blue"

    # Fix this line to use an f-string:
    message = ???

    assert "Jordan" in message, "Message should include the name"
    assert "14" in message, "Message should include the age"
    assert "blue" in message, "Message should include the favorite color"

    print(message)

if __name__ == "__main__":
    main()
