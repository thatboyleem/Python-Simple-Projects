alien_0={'color':'green', 'points':5} #dictionary declaration

print(alien_0['color']) #this returns a value associated with the key
print(alien_0['points'])

#dictionary is a collection of key-value pairs, each key is connected to a value
new_points = alien_0['points']
print(f"You Just earned {new_points} points!")

#adding new key-value pairs
alien_0['x_position']= 0
alien_0['y_position'] = 25
print(alien_0)

#starting with an empty dictionary
players ={}
players['mark']= 'center'
players['Number']= 5
players['Team']='Lakers'
print(players)

#modifying values in a dictionary
players['Team']="Mavs"
print(f"The players team is now {players['Team']}.")

alien_1 = {'X-position':0, 'y-position':25, 'speed':'medium'}
print(f"original position: {alien_1['X-position']}")

#move the alien to the right.
#determine how far to move the alien based on its current speed
if alien_1['speed'] =='slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    #this must be a fast alien
    x_increment = 3

#the new position is the old position plus the increment.
alien_1['X-position']=alien_1['X-position'] + x_increment
print(f"New Position: {alien_1['X-position']}")

#removing key-value pairs
players['nba all star']=9
print(players)

del players['nba all star'] #removing a key-value pair from a dictionary
print(players)

