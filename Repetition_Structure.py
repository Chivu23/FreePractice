# Loops
# Repetition structure

# IF
a = 7
if a == 7:
    print("a it's equal with 7")
else:
    print("a it's NOT equal with 7")


garage = ["Dacia", "Opel", "Audi", "Bmw"]
for cars in garage:
    print(f"My favorite car is {cars}")
    print(f"It's a good car!")
# --->  this loop will execute in total four times, one for each item,
#       and we can access the item by just referencing it by the variable
#       name that we used.

# FOR
for i in range(5):
    print(f"Looping {i} times!")

# WHILE
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Example of iteration variable")

