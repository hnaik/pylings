# Exercise: sets1
# Topic: Sets
#
# A set is a collection with NO duplicates.
# If you add the same item twice, it only keeps one copy.
# Great for finding unique items!
#
# Fix the code so the assertions pass.
#
# Hint: Use set() to convert a list to a set, which removes duplicates.


def main():
    visitors = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]

    # Convert to a set to get unique visitors only
    unique_visitors = ???

    assert isinstance(unique_visitors, set), "Should be a set"
    assert len(unique_visitors) == 3, f"Should have 3 unique visitors, got {len(unique_visitors)}"
    assert "Alice" in unique_visitors
    assert "Bob" in unique_visitors
    assert "Charlie" in unique_visitors

    print(f"Total visits: {len(visitors)}")
    print(f"Unique visitors: {len(unique_visitors)}")
    print(f"Who visited: {unique_visitors}")

if __name__ == "__main__":
    main()
