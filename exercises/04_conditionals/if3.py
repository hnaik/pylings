# Exercise: if3
# Topic: Elif (Else If)
#
# `elif` lets you check more than two possibilities.
# The first True condition wins!
#
# Fix the function to return a letter grade:
#   90 or above -> "A"
#   80-89 -> "B"
#   70-79 -> "C"
#   60-69 -> "D"
#   below 60 -> "F"
#
# Hint: if score >= 90: ... elif score >= 80: ... and so on


def get_grade(score):
    ???

def main():
    assert get_grade(95) == "A", f"Expected A, got {get_grade(95)}"
    assert get_grade(85) == "B", f"Expected B, got {get_grade(85)}"
    assert get_grade(75) == "C", f"Expected C, got {get_grade(75)}"
    assert get_grade(65) == "D", f"Expected D, got {get_grade(65)}"
    assert get_grade(50) == "F", f"Expected F, got {get_grade(50)}"

    print("Grade calculator is working!")
    for score in [95, 82, 71, 63, 45]:
        print(f"  Score {score}: {get_grade(score)}")

if __name__ == "__main__":
    main()
