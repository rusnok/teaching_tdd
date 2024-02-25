def f():
    return((1, 2))

# spravne rozbaleni (unpack)
a , b = f()
print(a, b)

# slozeny tuple
a, b = f(), 3
print(a)
print(b)

# klasicke prohozeni hodnot ve dvou promennych
a = 1
b = 2
c = a
a = b
b = c

# pythonovské prohozeni pomoci tuplu
print(a,b)
a , b = b, a
print(a, b)

# error
a, b = f(),
