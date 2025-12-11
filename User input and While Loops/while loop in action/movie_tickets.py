while True:
 age = input("Please Enter your age: ")
 if age.lower()=='quit':
       break
 age= int(age)
 if age <= 3:
        print("your ticket is free")
 elif age>3 and age <=12:
        print("your ticker is $10")
 else:
        print("Your ticket is $15")