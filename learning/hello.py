print("hello world")

x = None
x = 3
x = "obj c sucks"
type(x)

if x == 3:
    print("int")
elif x == "3":
    print("Str")
else:
    print("bleeehhhhhh")

some_list = [1,2,3,4,5, True, "Mike", False]

for x in some_list:
    print(x)

for x in range(1, 100, 5):
    print(x)

while x != 1001:
    print(x)
    x += 1


some_list_comprehension = [x for x in range(100) if x % 2 == 0]
