# Exercise: lists2
# Topic: Adding to Lists
#
# Lists can grow! Use .append() to add items to the end.
#
# Fix the code to add "Mango" to the fruits list.
#
# Hint: fruits.append("Mango")


def main():
    fruits = ["Apple", "Banana", "Cherry"]

    print(f"Before: {fruits}")
    ???  # Add "Mango" to the list

    assert len(fruits) == 4, f"Should have 4 fruits, got {len(fruits)}"
    assert fruits[-1] == "Mango", f"Last fruit should be Mango, got {fruits[-1]}"

    print(f"After: {fruits}")
    print(f"Total fruits: {len(fruits)}")

if __name__ == "__main__":
    main()
