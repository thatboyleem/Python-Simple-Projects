def build_profile(first, last, **userinfo):#the asterisk tells python to create a dictionary called userinfo
    """Build a dictionary containing everything we know about a user"""
    userinfo['first_name']=first
    userinfo['last_name']=last
    return userinfo
user_profile= build_profile('albert', 'einstein', location='Princeton', Field='physics')
print(user_profile)
