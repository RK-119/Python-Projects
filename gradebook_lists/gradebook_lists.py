last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
# print(gradebook)

# Adding 
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Modifiying the marks
gradebook[-1][-1] = 93 + 5

# Removing the marks 
gradebook[2].remove(85)

# Adding Result outcome
gradebook[2].append("Pass")

# Combining 2 lists
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
