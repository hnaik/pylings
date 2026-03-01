# Exercise: if2
# Topic: If and Else
#
# `else` runs when the `if` condition is False.
# Together they make sure one path always runs.
#
# Fix the function: if score >= 60, return "You passed!"
# Otherwise, return "Keep trying!"
#
# Hint: use if ... else ...


def check_score(score):
    ???

def main():
    assert check_score(75) == "You passed!", "75 should pass"
    assert check_score(60) == "You passed!", "60 should pass"
    assert check_score(59) == "Keep trying!", "59 should not pass"
    assert check_score(0) == "Keep trying!", "0 should not pass"

    print(f"Score 75: {check_score(75)}")
    print(f"Score 45: {check_score(45)}")
    print("Conditionals are working!")

if __name__ == "__main__":
    main()
