#1a Input a integer number and sum of digits
n=int(input("Nhap coi: "))
while (n <= 0):
        n=int(input("Nhap lai coi: "))
print(n)
#mylist = []
sum = 0
while True:
    sum += int(n % 10)
    n = int (n / 10)
    if(n < 1):
        break

"""for i in range(len(mylist)):
    sum+=mylist[i]"""
print(sum)