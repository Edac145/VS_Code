def remote_control_next():
    yield "cnn"
    yield "espn"

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

itr=remote_control_next()
print(next(itr))
print(next(itr))

for c in remote_control_next():
    print(c)

for f in fib():
    if f>50:
        break
    print(f)
