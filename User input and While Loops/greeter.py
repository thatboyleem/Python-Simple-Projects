prompt = "if you share your name, we can personalize the  message you see"
prompt += "\n what is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

#using int to accept numerical input
age = input("How Old are you? : ")
age = int(age)
if age>= 18:
    print(True)