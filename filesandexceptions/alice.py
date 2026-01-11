from pathlib import Path

path  = Path(r'C:\Users\King Leem\OneDrive\Desktop\Learn_python\filesandexceptions\alice.txt')
try:
    contents = path.read_text(encoding = 'utf-8') #we  use encoding argument when your systems default encoding system doesnt match the encoding of the file thats being read
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    #count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")