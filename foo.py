# x = 42
# def callf(func):
#     return func()

def countdown(n):
    def next():
        nonlocal n
        r = n
        n -= 1
        print(r)
        return r
    return next

next = countdown(10)
while True:
    v = next()
    if not v:
        break