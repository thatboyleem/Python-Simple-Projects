#use to take an action depending on different scenarios

age = 17
if age>=18:
    print("u are old enough to vote")
    print("have you registered yet")
else:
    print("Sorry You are too young to vote.")

#if-elif chain, used when you want to test for more two possible scenarios
age2=12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("You admission cost is $25")
else:
    print("Your admission Cost is $40")
#if you want only one block to run use an if-elif-else chain, if more than one block needs to run
#use independent if statements.

