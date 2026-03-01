# Exercise: dicts1
# Topic: Creating and Accessing Dictionaries
#
# A dictionary stores key-value pairs, like a real dictionary.
# word (key) -> definition (value)
#
# player["name"] gets the value for the "name" key.
#
# Fix the code so the assertions pass.
#
# Hint: Use the key name in square brackets to get the value.

# I AM NOT DONE

def main():
    player = {
        "name": "Hero",
        "level": 5,
        "health": 100,
        "score": 2500,
    }

    player_name = player[???]   # Should be "Hero"
    player_level = player[???]  # Should be 5
    player_score = player[???]  # Should be 2500

    assert player_name == "Hero", f"Got: {player_name}"
    assert player_level == 5, f"Got: {player_level}"
    assert player_score == 2500, f"Got: {player_score}"

    print(f"Player: {player_name}")
    print(f"Level: {player_level}")
    print(f"Score: {player_score}")

if __name__ == "__main__":
    main()
