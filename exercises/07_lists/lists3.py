# Exercise: lists3
# Topic: Looping Through Lists
#
# You can use a for loop to do something with every item in a list.
#
# Fix the code to print each item in the to-do list.
# Then calculate the total price of all items.
#
# Hint: for item in my_list: does the trick!

# I AM NOT DONE

def main():
    todo_list = ["Buy milk", "Do homework", "Walk the dog", "Read a book"]

    print("My to-do list:")
    for ??? in todo_list:
        print(f"  - {???}")

    prices = [2.50, 5.99, 1.25, 8.00]
    total = 0
    for price in prices:
        total = total + price

    assert round(total, 2) == 17.74, f"Total should be 17.74, got {total}"
    print(f"\nTotal cost: ${total:.2f}")

if __name__ == "__main__":
    main()
