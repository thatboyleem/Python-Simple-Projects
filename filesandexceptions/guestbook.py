from pathlib import Path

while input("Would you like to leave a message? (yes/no): ").lower() == 'yes':
    content = input("Enter your message: ")

    path = Path("guestbook.txt")
    with path.open(mode='a') as file:
        file.write(content + '\n')

    print("Your message has been added to the guestbook.\n")