indian_dummy_names = [
    "Aarav Sharma", "Veda Iyer", "Ishaan Patel", "Saanvi Kapoor", "Aditya Reddy",
    "Ananya Gupta", "Vikram Mehta", "Priya Rao", "Arjun Desai", "Neha Verma",
    "Rohit Singh", "Sneha Joshi", "Karan Shah", "Pooja Malhotra", "Sameer Agarwal",
    "Shreya Jain", "Rahul Yadav", "Kritika Choudhury", "Amit Kumar", "Rina Nair",
    "Ravi Mishra", "Tanya Kapoor", "Manish Gupta", "Swati Sharma", "Vishal Bhat",
    "Ayesha Khan", "Deepak Patil", "Tanvi Agarwal", "Siddharth Reddy", "Aarti Mehta",
    "Ankur Prasad", "Madhavi Rao", "Puneet Sharma", "Maya Verma", "Anil Kapoor",
    "Disha Patel", "Yash Rajput", "Kiran Das", "Divya Joshi", "Rajesh Saini",
    "Pallavi Singh", "Raghav Gupta", "Simran Bedi", "Nikhil Deshmukh", "Kavya Saxena",
    "Himanshu Kumar", "Neelam Kapoor", "Gaurav Tiwari", "Rekha Yadav", "Suman Nair"
]

ages = [25, 18, 29, 21, 25, 25, 30, 22, 19, 28, 20, 24, 25, 18, 21, 23, 27, 26, 20, 29, 20, 21, 23, 26, 24, 18, 28, 22, 27, 26, 22, 24, 23, 29, 20, 21, 25, 27, 29, 21, 23, 26, 20, 19, 22, 24, 28, 25, 23, 20]

# Consider that the numbers are the Age
# Tasks:
# 1. Print Names with Age Using For Loop ex: Vipin: 24 and so on

# for x in range(50):
    # print(indian_dummy_names[x], ages[0])
    # print(f"{indian_dummy_names[x]} : {ages[0]}")

# for x,y in zip(indian_dummy_names, ages):
#     print(f"{x} : {y}")


# 2. Make a new list that has elements in group of name and age ex: ("vipin", 24), ... and so on
# ("arav", 25)

# new_list = []

# for x,y in zip(indian_dummy_names, ages):
#     new_list.append((x,y))

#     print(new_list)

# new_list = [(x,y) for x, y in zip (indian_dummy_names, ages)]
# print(new_list)


# 3. Remove all duplicate data from the Age List
# new_list = list(set(ages))
# print(new_list)

# for x in zip(indian_dummy_names, ages):
#     print(x)

# 4. Get all Names Above 20 years by combining the Age and Numbers
# for x, y in zip(indian_dummy_names, ages):
#     if y > 20:
#         print(x,y)

# * Get All Names Who Are Of 30 Years

# for x, y in zip(indian_dummy_names, ages):
#     if y == 30:
#         print(x,y)