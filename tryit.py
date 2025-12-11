guest_list =['farash', 'nabil', 'brosk']
print("You can only bring two people to dinner")
print(f'hello {guest_list[0].title()}, you are cordially invited to a dinner party on the 10th of this month')
print(f'hello {guest_list[1].title()}, you are cordially invited to a dinner party on the 10th of this month')
print(f'hello {guest_list[-1].title()}, you are cordially invited to a dinner party on the 10th of this month')

guest_list[-1]= 'Ella'
#print(f'hello {guest_list[-1].title()}, you are cordially invited to a dinner party on the 10th of this month')

guest_list.insert(-1,'Hasi')
guest_list.insert(-2, 'Mimi')
guest_list.insert(0, 'mark')
guest_list.append('baba')
print(f'hello {guest_list[0].title()}, you are cordially invited to a dinner party on the 10th of this month')
print(f'hello {guest_list[1].title()}, you are cordially invited to a dinner party on the 10th of this month')
print(f'hello {guest_list[2].title()}, you are cordially invited to a dinner party on the 10th of this month')
print(f'hello {guest_list[3].title()}, you are cordially invited to a dinner party on the 10th of this month')
print(f'hello {guest_list[4].title()}, you are cordially invited to a dinner party on the 10th of this month')
print(f'hello {guest_list[5].title()}, you are cordially invited to a dinner party on the 10th of this month')
print(f'hello {guest_list[6].title()}, you are cordially invited to a dinner party on the 10th of this month')
print(guest_list)

deleted_guest= guest_list.pop(2)
#deleted_guest= guest_list.pop(1)
#deleted_guest= guest_list.pop(2)
#deleted_guest= guest_list.pop(3)
#deleted_guest= guest_list.pop(4)

#removing elements from a list using del
del guest_list[0] #pass the index

#removing elements from list using remove
guest_list.remove('nabil') #used when u want to remove by value and dont know the position of a item in a list

print(deleted_guest)
print(guest_list)