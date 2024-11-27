print("The For Loop program is :")
n = 10
for i in range(1, n + 1):
    print("* " * i)


print("The x==y program is :")
x = 2
y = 6
while x != y:
    if x < y:
        x += 1
    elif x > y:
        x -= 1
    print(f"x = {x}, y = {y}")
print("The program will end at : x == y")
