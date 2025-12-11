books = ['rich dad', 'love', 'python crash course', 'freeman']

for book in books:
    if book =='love': #used for comparison to check if a a value(s) is true or equal
        print(book.upper())
    else:
        print(book.title())


requested_topping = 'pepperoni'

if requested_topping != 'mushroom':
    print("Hold the mushroom")

#checking multiple conditions
car='subaru'
print("is car=='subaru'? i predict true")
print(car=='subaru') #checks if the statement is true

print("\nis car== 'audi'? I predict false.")
print(car == 'audi')

age=19
if age>= 18:
    print("u are old enough to vote")
