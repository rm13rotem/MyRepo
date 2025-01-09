# Create a dictionary
student_info = {
    "name": "John",
    "age": 7,
    "grade": 1,
    "favorite_subject": "Science"
}

# Accessing values
print(student_info["name"])  # Output: John
print(student_info["age"])   # Output: 7

# Adding a new key-value pair
student_info["hobby"] = "Reading"
print(student_info)

# Modifying an existing value
student_info["grade"] = 2
print(student_info)

# Deleting a key-value pair
del student_info["age"]
print(student_info)

# Loop through dictionary
for key, value in student_info.items():
    print(f"{key}: {value}")
    