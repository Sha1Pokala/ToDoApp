# Practice Time
# Contact Directory:
# Create a dictionary to store names and phone numbers.
# Add a new contact.
# Remove an existing contact.
# Print the updated contact list.

people = {
    "person1": {
        "name": "Shashank",
        "city": "Sanford",
        "Phone_number":9404358630
    },
    "person2": {
        "name": "Likhita",
        "city": "Orlando",
        "Phone_number":3147230153
    },
    "person3": {
        "name": "Rahul",
        "city": "New York",
        "Phone_number":0000000000
    }
}
#Adding a person to the dictionary
people["person4"] = {
    "name": "Bhupesh",
    "city": "Miami",
    "Phone_number":1111111111
}

#deleting person 3 from the dictionary
people.pop("person3")

#printing thr complete list after performing the operations
print(people)

