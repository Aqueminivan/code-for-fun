def do_twice(f, x):
    f(x)
    f(x)

def add2(x):
    x += 2
    print(x)

def do_four(f, x):
    do_twice(f, x)
    do_twice(f, x)

do_twice(add2, 1)
print("=====")
do_four(add2, 1)
