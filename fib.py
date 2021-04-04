password = "qwertyuiop"
def check_password(func):
    counter = 0
    def wrapper(*args,**kwargs):
        nonlocal counter
        if counter == 0:
            a = input()
            if a == password:
                counter += 1
                return func(*args, **kwargs)
            else:
                print("В доступе отказано")
        else:
            return func(*args, **kwargs)
    return wrapper



@check_password
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))