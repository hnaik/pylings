# Exercise: classes1
# Topic: Creating a Class
#
# A class is like a blueprint for creating objects.
# Each object made from the class is called an "instance".
#
# Fix the Pet class to have a name and animal_type.
#
# Hint:
# class Pet:
#     def __init__(self, name, animal_type):
#         self.name = name
#         self.animal_type = animal_type


class Pet:
    def __init__(self, ???):
        self.name = ???
        self.animal_type = ???

def main():
    my_pet = Pet("Whiskers", "cat")
    your_pet = Pet("Buddy", "dog")

    assert my_pet.name == "Whiskers", f"Got: {my_pet.name}"
    assert my_pet.animal_type == "cat", f"Got: {my_pet.animal_type}"
    assert your_pet.name == "Buddy", f"Got: {your_pet.name}"

    print(f"My pet: {my_pet.name} the {my_pet.animal_type}")
    print(f"Your pet: {your_pet.name} the {your_pet.animal_type}")

if __name__ == "__main__":
    main()
