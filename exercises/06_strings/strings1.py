# Exercise: strings1
# Topic: String Indexing
#
# A string is a sequence of characters.
# You can get a single character using its index (position number).
# Counting starts at 0!
#
# "Hello"[0] gives "H"
# "Hello"[1] gives "e"
#
# Fix the assertions below.
#
# Hint: Python starts counting at 0, not 1!

# I AM NOT DONE

def main():
    word = "Python"

    first_letter = word[???]  # Should be "P"
    last_letter = word[???]   # Should be "n"
    third_letter = word[???]  # Should be "t"

    assert first_letter == "P", f"Expected P, got {first_letter}"
    assert last_letter == "n", f"Expected n, got {last_letter}"
    assert third_letter == "t", f"Expected t, got {third_letter}"

    print(f"First: {first_letter}, Last: {last_letter}, Third: {third_letter}")
    print("String indexing works!")

if __name__ == "__main__":
    main()
