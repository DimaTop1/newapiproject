def printUpper(func):
    def wrapper(*args,**kwargs):
        a = []
        for arg in args:
            a.append(str(arg).upper())
        truea = " ".join(a)
        func(truea, **kwargs)
    return wrapper
print = printUpper(print)
print("llol",1,'a',sep=',',end='|')
