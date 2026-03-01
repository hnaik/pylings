# Exercise: modules1
# Topic: Importing Modules
#
# Python comes with lots of built-in tools called modules.
# Use `import` to bring them in.
# The `math` module has useful math functions!
#
# Fix the code to use the math module.
#
# Hint: import math   then use math.sqrt(), math.pi, math.floor()

# I AM NOT DONE

???  # Import the math module

def main():
    # math.sqrt gives the square root
    root = math.sqrt(25)
    assert root == 5.0, f"sqrt(25) should be 5.0, got {root}"

    # math.pi is the value of pi
    circumference = 2 * math.pi * 5  # circle with radius 5
    assert round(circumference, 2) == 31.42, f"Got {round(circumference, 2)}"

    # math.floor rounds down
    floored = math.floor(3.9)
    assert floored == 3, f"floor(3.9) should be 3, got {floored}"

    print(f"Square root of 25: {root}")
    print(f"Circumference: {round(circumference, 2)}")
    print(f"Floor of 3.9: {floored}")
    print("Math module imported successfully!")

if __name__ == "__main__":
    main()
