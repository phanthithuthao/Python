# Input a integer number
def input_number_int():
    n=int(input("Nhap coi: "))
    while (n <= 0):
        n=int(input("Nhap lai coi: "))
    return n

#1a Sum of digits

#mylist = []
n = int(input_number_int())
m = n
sum = 0
while True:
    sum += int(n % 10)
    n = int (n / 10)
    if(n < 1):
        break

"""for i in range(len(mylist)):
    sum+=mylist[i]"""
print(sum)

#1b Product of even digits

mul = 1
while True:
    temp = m % 10
    if(temp % 2 == 0):
        mul *= temp
    m = int (m / 10)
    if(m < 1):
        break
print(mul)