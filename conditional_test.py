string1 = "mark"
string2 = "Mark"

print(string1 == string2)
print(string2.lower()== string1)

age1= 30
age2 = 12

print(age2 >= 11 or age1 <=30)

courses =['maths', 'chemistry', 'physics', 'programming', 'statistics']
cse4107 = 'Java progamming'

if cse4107 not in courses:
    print(f"{cse4107.title()}, you can take it as an Elective if you want")