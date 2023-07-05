# Input a integer number
def input_number_int():
    n=int(input("Nhap coi: "))
    while (n <= 0):
        n=int(input("Nhap lai coi: "))
    return n

#1a Sum of digits

#mylist = []
n = int(input_number_int())
val = n
sum = 0
while True:
    sum += int(val % 10)
    val = int (val / 10)
    if(val < 1):
        break

"""for i in range(len(mylist)):
    sum+=mylist[i]"""
print(sum)

#1b Product of even digits
val = n
mul = 1
while True:
    temp = val % 10
    if(temp % 2 == 0):
        mul *= temp
    val = int (val / 10)
    if(val < 1):
        break
print(mul)

#1c count odd numbers
val = n
count = 0
while True:
    temp = val % 10
    if(temp % 2 != 0):
        count += 1
    val = int (val / 10)
    if(val < 1):
        break
print(count)

#1d Find max number
val = n
max = -1
while True:
    temp = val % 10
    if(temp > max):
        max = temp
    val = int (val / 10)
    if(val < 1):
        break
print(max)