Password = "go"

def check_password(func):
    def wrapper(*args,**kwargs):
        a = input()
        if a == Password:
            func(*args,**kwargs)
        else:
            print("В доступе отказано")
    return wrapper

@check_password
def clown():
    print("победа")

clown()