# Exercise: files2
# Topic: Reading from Files
#
# You can also read text from existing files.
# Use `with open(filename, "r") as f:` to read.
# The "r" means "read mode".
#
# Fix the code to read from a file.
#
# Hint:
# with open(filename, "r") as f:
#     content = f.read()


import os

def main():
    filename = "/tmp/pythonlings_read_test.txt"

    # First, create a file to read from
    with open(filename, "w") as f:
        f.write("Python is awesome!\nKeep learning!\nYou got this!")

    # Now read the file
    ???

    assert "Python is awesome!" in content, "Should find first line"
    assert "Keep learning!" in content, "Should find second line"

    lines = content.split("\n")
    assert len(lines) == 3, f"Should have 3 lines, got {len(lines)}"

    print("File contents:")
    for line in lines:
        print(f"  {line}")
    print("File reading works!")

    # Clean up
    os.remove(filename)

if __name__ == "__main__":
    main()
