prompt = "\nTell me something and i'll repeat back to you: "
prompt += "\n Enter 'Quit' to end program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit': 
     print(message)