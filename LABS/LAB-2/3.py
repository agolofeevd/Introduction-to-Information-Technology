def max_of_two(number):
    a = int(input('x: '))
    b = int(input('y: '))
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "x=y"
print( max_of_two(1))
