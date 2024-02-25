def add_numbers(a: int, b: int):
    return a + b

def sum_args(max_value, *args):
    soucet = 0
    max_value = max_value if isinstance(max_value, int) else 100
    for a in args:
        if isinstance(a, int) and a < max_value:
            soucet += a
    return soucet

def capital_case(x):
    if isinstance(x, int):
        raise TypeError("Integer is wrong type")
    return x.capitalize()

def odd_indexes(string):
    return str(string)[1::2]

#sum_args(5, 5, 'asdf')
#a = [5, 'asdf']
#sum_args(5, *a)

#print(odd_indexes(123))

