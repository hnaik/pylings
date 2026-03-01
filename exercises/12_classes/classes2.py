# Exercise: classes2
# Topic: Class Methods
#
# Methods are functions that belong to a class.
# They always start with `self` as the first parameter.
#
# Add a speak() method to the Pet class.
# It should print "<name> says: Woof!" (or Meow!, etc.)
#
# Hint:
# def speak(self):
#     print(f"{self.name} says: {self.sound}!")

# I AM NOT DONE

class Pet:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        ???

def main():
    dog = Pet("Rex", "Woof")
    cat = Pet("Luna", "Meow")

    dog.speak()
    cat.speak()

    print("Your pets can speak!")

if __name__ == "__main__":
    main()
