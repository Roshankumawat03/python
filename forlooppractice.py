# Use this data as a template:


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
# And do below tasks:
# 1. Count the Names Starting From A
count_name = 0
for name in indian_dummy_names:
    if name.startswith("A"): 
     print(name)
     count_name += 1
     print(count_name)
    

# 2. Count Total Number Of Names In The List

# print(len(indian_dummy_names))   # Output: 50

# 3. Print Surname Of All The Names

# for name in indian_dummy_names:
#     for x in name.split():
#         if x != name.split()[0]:
#             print(x)

#Output: ['Sharma', 'Iyer', 'Patel', 'Kapoor', 'Reddy', 'Gupta', 'Mehta', 'Rao', 'Desai', 'Verma', 'Singh', 'Joshi', 'Shah', 'Malhotra', 'Agarwal', 'Jain', 'Yadav', 'Choudhury', 'Kumar', 'Nair', 'Mishra', 'Kapoor', 'Gupta', 'Sharma', 'Bhat', 'Khan', 'Patil', 'Agarwal', 'Reddy', 'Mehta', 'Prasad', 'Rao', 'Sharma', 'Verma', 'Kapoor', 'Patel', 'Rajput', 'Das', 'Joshi', 'Saini', 'Singh', 'Gupta', 'Bedi', 'Deshmukh', 'Saxena', 'Kumar', 'Kapoor', 'Tiwari', 'Yadav', 'Nair']

# 4. Print All Names Starting From Y

# for name in indian_dummy_names:
#    if name.startswith("Y"):
#     print(name)    # Output: Yash Rajput

# 5. Print All Names Ending From a

# for name in indian_dummy_names:
#    if name.endswith("a"):
#       print(name)

#Output: ['Aarav Sharma', 'Ananya Gupta', 'Vikram Mehta', 'Neha Verma', 'Pooja Malhotra', 'Ravi Mishra', 'Manish Gupta', 'Swati Sharma', 'Aarti Mehta', 'Puneet Sharma', 'Maya Verma', 'Raghav Gupta', 'Kavya Saxena']

# 6. Print All Names In Capital Latters
# for name in indian_dummy_names:
#     print(name.upper())

# Output: ['AARAV SHARMA', 'VEDA IYER', 'ISHAAN PATEL', 'SAANVI KAPOOR', 'ADITYA REDDY', 'ANANYA GUPTA', 'VIKRAM MEHTA', 'PRIYA RAO', 'ARJUN DESAI', 'NEHA VERMA', 'ROHIT SINGH', 'SNEHA JOSHI', 'KARAN SHAH', 'POOJA MALHOTRA', 'SAMEER AGARWAL', 'SHREYA JAIN', 'RAHUL YADAV', 'KRITIKA CHOUDHURY', 'AMIT KUMAR', 'RINA NAIR', 'RAVI MISHRA', 'TANYA KAPOOR', 'MANISH GUPTA', 'SWATI SHARMA', 'VISHAL BHAT', 'AYESHA KHAN', 'DEEPAK PATIL', 'TANVI AGARWAL', 'SIDDHARTH REDDY', 'AARTI MEHTA', 'ANKUR PRASAD', 'MADHAVI RAO', 'PUNEET SHARMA', 'MAYA VERMA', 'ANIL KAPOOR', 'DISHA PATEL', 'YASH RAJPUT', 'KIRAN DAS', 'DIVYA JOSHI', 'RAJESH SAINI', 'PALLAVI SINGH', 'RAGHAV GUPTA', 'SIMRAN BEDI', 'NIKHIL DESHMUKH', 'KAVYA SAXENA', 'HIMANSHU KUMAR', 'NEELAM KAPOOR', 'GAURAV TIWARI', 'REKHA YADAV', 'SUMAN NAIR']

