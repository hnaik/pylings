# Exercise: dicts3
# Topic: Looping Through Dictionaries
#
# Use .items() to loop through both keys and values.
# for key, value in my_dict.items():
#
# Fix the loop to print each subject and grade.
#
# Hint: for subject, grade in grades.items(): then print them!

# I AM NOT DONE

def main():
    grades = {
        "Math": 92,
        "Science": 88,
        "English": 95,
        "History": 79,
    }

    print("My grades:")
    for ??? in grades.items():
        print(f"  {???}: {???}")

    # Find the highest grade
    best_subject = max(grades, key=grades.get)
    assert best_subject == "English", f"Best subject should be English, got {best_subject}"

    print(f"\nBest subject: {best_subject} ({grades[best_subject]})")

if __name__ == "__main__":
    main()
