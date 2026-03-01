# Exercise: files1
# Topic: Writing to Files
#
# Python can create and write to files on your computer!
# Use `with open(filename, "w") as f:` to create/write a file.
# The "w" means "write mode".
# The `with` statement closes the file automatically.
#
# Fix the code to write a message to a file.
#
# Hint:
# with open("my_file.txt", "w") as f:
#     f.write("Hello, file!")

# I AM NOT DONE

import os

def main():
    filename = "/tmp/pythonlings_test.txt"

    # Write "Hello from Pythonlings!" to the file
    ???

    # Check the file was created and has content
    assert os.path.exists(filename), "File was not created!"
    with open(filename, "r") as f:
        content = f.read()
    assert "Hello from Pythonlings!" in content, f"File content: {content}"

    print(f"File created: {filename}")
    print(f"Content: {content}")
    print("File writing works!")

    # Clean up
    os.remove(filename)

if __name__ == "__main__":
    main()
