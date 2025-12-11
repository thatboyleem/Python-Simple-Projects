def build_profile(first, last, **userinfo):
    """this function is to make a user profile with an additional info"""
    userinfo['first_name']= first
    userinfo['last_name']= last
    return userinfo

user_profile = build_profile('saleem', 'ahmed', city='Dhaka', BSc='CSE', hobby='Basketball')
print(user_profile)

def make_car(manufacturer, model, **car_info):
    """this is a function to make a car with an arbitrary number of keywords"""
    car_info['manufacturer']=manufacturer
    car_info['model']=model
    return car_info

car= make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)