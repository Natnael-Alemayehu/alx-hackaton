def adder(*args):
    total = 0
    for i in args:
        total += i

    return total

print(adder(1,2,3))
