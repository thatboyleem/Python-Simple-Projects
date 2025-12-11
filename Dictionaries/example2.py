# Create a dictionary of persons and their favorite numbers
favorite_numbers = {
    'John': [7, 13, 21],
    'Emily': [4, 9, 15],
    'Michael': [2, 8, 10],
    'Sarah': [5, 11, 14],
    'Anna': [3, 6, 12]
}

# Print each person's name along with their favorite numbers
for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are: {', '.join(str(number) for number in numbers)}")
