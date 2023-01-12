# A list of tuples representing the names and ages of people
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20), ("David", 35)]

# A callback function that sorts the list of people by age
people.sort(key=lambda person: person[1])

# The list of people is now sorted by age
print(people)
# Output: [("Charlie", 20), ("Alice", 25), ("Bob", 30), ("David", 35)]

print(type(lambda person: person[1]))  # <class 'function'>

# Question - there is not lambda data object / type?
