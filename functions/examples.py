def make_shirt(size, message):
    """this is a function that displays info about a shirt design"""
    print(f"Your size is {size}")
    print(f"Your message is {message}\n")

while True:
    s_z= input("please enter a size: ")
    design= input("please enter a message: ")

    print("----Here Are Your Designs-------")
    make_shirt(s_z, design)

    prompt= input("Would you like to make another design?(y/n): ")
    if prompt == 'N':
        break
