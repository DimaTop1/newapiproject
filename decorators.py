import time
user = {
    'name': 'timur',
    'access_level': 'admin'
}


def secure_function(func):
    def wrapper(*args, **kwargs):
        if user['access_level'] == 'admin':
            return func(*args, **kwargs)
        return 'Access denied'

    return wrapper


@secure_function
def get_secure_information():
    return 'My super password is qwerty123'

def printUpper(func):
    def wrapper():
        func.upper()
    return wrapper
print = printUpper(get_secure_information())
print()