def make_sandwich(*items):
    """this function is to accept a list of items from the user for their sandwich"""
    print(f"this is a summary of your order: ")
    for sandwich in items:
        print(f"\t-{sandwich}")

#sandwich = ('cheese', 'burger', 'mayonaise', 'lettuce')
make_sandwich('cheese', 'butter', 'lettuce', 'tomatoe slice')