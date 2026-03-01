# Exercise: tuples1
# Topic: Tuples
#
# A tuple is like a list, but you CANNOT change it once created.
# Use parentheses ( ) to create a tuple.
# This is useful when data should never change, like a GPS location.
#
# Fix the assertions below.
#
# Hint: coordinates = (latitude, longitude) - use parentheses!


def main():
    # A GPS coordinate - latitude and longitude
    location = ???  # Create a tuple with values (40.7128, -74.0060)

    assert isinstance(location, tuple), "location should be a tuple"
    assert location[0] == 40.7128, f"Latitude should be 40.7128, got {location[0]}"
    assert location[1] == -74.0060, f"Longitude should be -74.0060, got {location[1]}"
    assert len(location) == 2, "Should have 2 values"

    print(f"Location: {location}")
    print(f"Latitude: {location[0]}")
    print(f"Longitude: {location[1]}")
    print("Tuples are like locked lists!")

if __name__ == "__main__":
    main()
