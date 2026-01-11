from pathlib import Path

content= input("Enter your message: ")


path = Path("guest.txt")
path.write_text(content)