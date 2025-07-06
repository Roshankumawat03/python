# Grade Calculator
# Write a program that takes a student's score (0–100) and prints the corresponding letter grade (A, B, C, D, or F).

score = int(input("Enter Your Score: "))

# 90+ A
# 80+ B
# 70+ C
# 60+ D 
# >60 F

if score >= 90:
 print("A")
elif score >= 80:
 print("B")
elif score >= 70:
 print("C")
elif score >= 60:
 print("D")
else:
 print("F")
 