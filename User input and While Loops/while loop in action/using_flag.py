#u can define one variable that determines whether or not the entire program is active
#a flag acts as a signal to program

prompt = "\nTell me something and i'll repeat back to you: "
prompt += "\n Enter 'Quit' to end program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)