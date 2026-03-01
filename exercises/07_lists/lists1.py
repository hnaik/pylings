# Exercise: lists1
# Topic: Creating and Accessing Lists
#
# A list holds multiple items in order.
# Use square brackets [ ] to create a list.
# Use the index (position number) to access items.
# Remember: counting starts at 0!
#
# Fix the code so the assertions pass.
#
# Hint: songs[0] gets the first song, songs[2] gets the third.

# I AM NOT DONE

def main():
    songs = ["Shake It Off", "Blinding Lights", "Stay", "Shape of You"]

    first_song = songs[???]   # Should be "Shake It Off"
    third_song = songs[???]   # Should be "Stay"

    assert first_song == "Shake It Off", f"Got: {first_song}"
    assert third_song == "Stay", f"Got: {third_song}"
    assert len(songs) == 4, "There should be 4 songs"

    print(f"My playlist has {len(songs)} songs.")
    print(f"First song: {first_song}")
    print(f"Third song: {third_song}")

if __name__ == "__main__":
    main()
