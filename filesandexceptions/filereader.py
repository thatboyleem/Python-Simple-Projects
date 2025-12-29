from pathlib import Path
path = Path(r"C:\Users\King Leem\OneDrive\Desktop\Learn_python\filesandexceptions\pi_digits.txt")
contents = path.read_text()
lines = contents.splitlines()

for line in lines:
    print(line)