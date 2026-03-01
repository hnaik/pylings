# Exercise: dicts2
# Topic: Modifying Dictionaries
#
# You can add new keys or update existing ones in a dictionary.
# my_dict["new_key"] = "new_value"
#
# Fix the code to add the missing information to the contact card.
#
# Hint: contact["email"] = "alex@example.com"

# I AM NOT DONE

def main():
    contact = {
        "name": "Alex",
        "phone": "555-1234",
    }

    # Add email and city to the contact
    contact[???] = "alex@example.com"
    contact[???] = "Springfield"

    assert "email" in contact, "contact should have an email"
    assert "city" in contact, "contact should have a city"
    assert contact["email"] == "alex@example.com"
    assert contact["city"] == "Springfield"

    print("Contact card:")
    for key, value in contact.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    main()
