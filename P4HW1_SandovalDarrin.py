# Darrin Sandoval
# April 19, 2026
# P4HW1
# This program collects a user-specified number of scores, validates them (0-100),
# drops the lowest score, calculates the average, and displays the corresponding letter grade.

# Pseudocode:
# 1. Ask user how many scores they want to enter
# 2. Create an empty list to store scores
# 3. Use a loop to collect the desired number of scores:
#       - Use an inner loop to keep asking until a valid score (0-100) is entered
#       - Add valid score to the list
# 4. Find the lowest score in the list
# 5. Create a new list with the lowest score removed
# 6. Calculate the average of the modified list
# 7. Determine the letter grade based on the average
# 8. Display: lowest score, modified score list, average, and letter grade

# Get number of scores from user
num_scores = int(input("How many scores do you want to enter? "))

scores = []

# Collect scores with validation
for i in range(num_scores):
    while True:
        score = float(input(f"Enter score #{i+1}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print()

# Process the scores
lowest_score = min(scores)
modified_scores = [s for s in scores if s != lowest_score]  # Remove one instance of lowest score

average = sum(modified_scores) / len(modified_scores)

# Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Display results
print("\n--------------Results--------------")
print(f"Lowest Score  : {lowest_score:.1f}")
print(f"Score List    : {modified_scores}")
print(f"Average Score : {average:.2f}")
print(f"Grade         : {grade}")
print("-----------------------------------")