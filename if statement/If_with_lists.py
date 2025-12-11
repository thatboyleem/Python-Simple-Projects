#checking for special items
requested_toppings =['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we are out of green peppers right now")
    else:
      print(f"adding {requested_topping} topping")
print('\nfinished making your pizza')


#checking that a list is  not empty
requested_books = []
if requested_books: #checks if list contains atleast one item, an empty evaluates to false
   for book in requested_books:
      print(f"selecting {book}")
   print('finished selecting')
else:
   print("\nare you sure u dont want any book?")

#using  multiple lists
avalaible_foods=['mushrooms', 'olives', 'green peppers', 'pepperoni','pineapple', 'extra cheese']

req_foods =['mushrooms', 'french fries', 'extra cheese']

for req_food in req_foods:
   if req_food in avalaible_foods:
      print(f"adding {req_food}.")
   else:
      print(f"sorry we dont have {req_food}")
print("\n Finished Preparing your order")
   