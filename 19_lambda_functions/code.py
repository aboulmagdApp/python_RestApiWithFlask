add = lambda x, y: x + y

print(add(10,6))


def double(x):
    return x * 2

sequence = [1,3,5,9,8]
# when use nourmal function
#doubled  = [double(x) for x in sequence]
# when use lambda 
#doubled  = [(lambda x: x * 2)(x) for x in sequence]
# when use map
doubled = list(map(lambda x: x * 2, sequence))

print(doubled)