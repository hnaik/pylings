# Exercise: modules2
# Topic: The random Module
#
# The `random` module helps you pick random things.
# Great for games, simulations, and surprises!
#
# Fix the code to use the random module.
#
# Hint:
# random.randint(1, 6) picks a random number from 1 to 6
# random.choice(my_list) picks a random item from a list

# I AM NOT DONE

???  # Import the random module

def main():
    # Set a seed so results are predictable for testing
    random.seed(42)

    # Roll a dice (1 to 6)
    roll = random.randint(???)
    assert 1 <= roll <= 6, f"Roll should be 1-6, got {roll}"

    # Pick a random snack
    snacks = ["apple", "chips", "yogurt", "banana", "granola bar"]
    snack = random.choice(???)
    assert snack in snacks, f"Snack should be from the list, got {snack}"

    print(f"You rolled: {roll}")
    print(f"Random snack: {snack}")
    print("Random module works!")

if __name__ == "__main__":
    main()
