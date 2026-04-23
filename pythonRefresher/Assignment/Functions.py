"""Functions Assignment
- Create a function that takes in 3 parameters(firstname, lastname, age) and
returns a dictionary based on those values
    """
    
def create_user(firstname, lastname, age):
    user_info = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return user_info

new_user = create_user("shahd", "haider", 24)

print(new_user)
