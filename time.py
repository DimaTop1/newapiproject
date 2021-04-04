import time
def time_check(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(f'{end-start}'+"секунд")
    return wrapper()

@time_check
def k():
    a = 1
    b = a*2
    c = b**4
    d = c*4+b**6+a
    print(a,b,c,d,sep=" ")
    print(1+2+3)