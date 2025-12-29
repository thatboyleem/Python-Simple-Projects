from Dice import Die

die20= Die(sides=20)
for i in range(10):
    print(f"Roll {i+1}: {die20.roll()}")