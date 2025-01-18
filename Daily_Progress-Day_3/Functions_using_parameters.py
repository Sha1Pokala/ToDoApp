# Create a Greeting Function: Write a function that takes a name and a time of day (e.g., "morning", "afternoon") 
# as parameters and returns a greeting like:"Good morning, Shashank!"

def morning (name):
    return f"Good morning, {name} !!"

def afternoon (name):
    return f"Good after noon, {name} !!"

def evening (name):
    return f"Good evening, {name} !!"

def night (name):
    return f"Good Night, {name} !!"

# taking input from the user

name =str(input("Enter you good name- "))
time_of_day = input("Enter the time of day (morning, afternoon, evening, night): ").lower()

# Calling the appropriate function based on user input
if time_of_day == "morning":
    print(morning(name))
elif time_of_day == "afternoon":
    print(afternoon(name))
elif time_of_day == "evening":
    print(evening(name))
elif time_of_day == "night":
    print(night(name))
else:
    print("Invalid time of day entered.")
