#used to exit a loop immediately without running any remaining code in the loop
#regardless of the results in the loop

prompt = "\n Please enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city =='quit':
        break
    else:
        print(f"I'd love to visit {city.title()}!")
