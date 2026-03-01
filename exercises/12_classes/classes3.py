# Exercise: classes3
# Topic: Classes with More Methods
#
# Classes can have multiple methods that work together.
# Use self to access and change the object's data.
#
# Fix the Player class to track score.
#
# Hint: self.score += points to add points


class Player:
    def __init__(self, name):
        self.name = name
        self.score = ???  # Start at 0

    def add_points(self, points):
        ???  # Add points to self.score

    def get_score(self):
        return self.score

def main():
    player1 = Player("Alex")
    assert player1.score == 0, "Should start at 0"

    player1.add_points(10)
    assert player1.get_score() == 10, f"Should be 10, got {player1.get_score()}"

    player1.add_points(25)
    assert player1.get_score() == 35, f"Should be 35, got {player1.get_score()}"

    print(f"{player1.name}'s score: {player1.get_score()}")
    print("Player class works!")

if __name__ == "__main__":
    main()
