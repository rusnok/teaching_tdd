a = [1, 2, 3]
b = [10, 20, 30]

for x, y in zip(a, b):
    print(x)
    print(y)

print("-------")
for x in a:
    for y in b:
        print(x)
        print(y)