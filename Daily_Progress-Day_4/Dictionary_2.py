# Student Marks:
# Create a dictionary with student names as keys and their marks as values.
# Find the average marks of all students.


Student={

    "Shashank":{
        "English":90,
        "Hindi":93,
        "Maths":100,
        "Science":95,
        "Social":98
    },

    "Likhita":{
        "English":30,
        "Hindi":76,
        "Maths":45,
        "Science":79,
        "Social":76
    },

    "Rahul": {
        "English": 76, 
        "Hindi": 57, "Maths": 34, 
        "Science": 99, 
        "Social": 96
    },
    "Anjali":{
        "English": 37, 
        "Hindi": 38, 
        "Maths": 52, 
        "Science": 96, 
        "Social": 32
    },
    "Aryan":{
        "English": 88, 
        "Hindi": 37, 
        "Maths": 41, 
        "Science": 48, 
        "Social": 51
    },
    "Riya": {"English": 68, "Hindi": 72, "Maths": 88, "Science": 80, "Social": 66},
    "Kunal": {"English": 30, "Hindi": 67, "Maths": 97, "Science": 58, "Social": 70},
    "Neha": {"English": 73, "Hindi": 92, "Maths": 64, "Science": 77, "Social": 98},
    "Rohan": {"English": 63, "Hindi": 76, "Maths": 96, "Science": 63, "Social": 91},
    "Simran": {"English": 83, "Hindi": 69, "Maths": 79, "Science": 37, "Social": 92}
}

# Initialize a dictionary to store total marks for each subject
subject_totals = {"English": 0, "Hindi": 0, "Maths": 0, "Science": 0, "Social": 0}

# Count the number of students
num_students = len(Student)

# Calculate total marks for each subject
for marks in Student.values():
    for subject, score in marks.items():
        subject_totals[subject] += score

# Calculate average marks for each subject
subject_averages = {subject: total / num_students for subject, total in subject_totals.items()}

# Display the average marks for each subject
print(subject_averages)

