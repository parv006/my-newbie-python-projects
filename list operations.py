x = 1
li = []

while x == 1:
    p = input('Enter a number: ')
    print('Do you want to continue adding numbers?')
    x = int(input('Write 1 for yes and 0 for no: '))
    li.append(p)

print('Here are your entered numbers:')
print(li)

if len(li) < 2:
    print("You only entered 1 number. An arithmetic operation cannot be performed on just one number.")
else:
    print("Do you want to perform arithmetic operations on the given list?")
    xi = int(input("Write 1 for yes and 0 for no: "))

li1 = []
l = len(li) - 1

for p in range(l):
    exp = input(f"Enter the symbol for the mathematical operation between index {p} and index {p + 1}: ")
    li1.append(exp)

print("Operation symbols:", li1)

# Combine numbers and operation symbols
final = []
for r in range(len(li)):
    final.append(li[r])
    if r < len(li1):
        final.append(li1[r])

print("Combined list:", ''.join(final))