# Student Grade Calculator

name = input("Enter student name: ")

m1 = float(input("Enter mark 1 (0-100): "))
m2 = float(input("Enter mark 2 (0-100): "))
m3 = float(input("Enter mark 3 (0-100): "))

total = m1 + m2 + m3
percentage = (total / 300) * 100

# Grade Logic
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print("\n----- Student Report -----")
print(name)
print(f"Total: {total}/300")
print(f"Percentage: {percentage:.2f}%")
print("Grade:", grade)
