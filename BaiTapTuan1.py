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
    sum += val % 10
    val = val // 10
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
    if(temp % 2 == 0 and temp > 0):
        mul *= temp
    val = val // 10
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
    val = val // 10
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
    val = val // 10
    if(val < 1):
        break
print(max)

#1e Find min number
val = n
min = n % 10
while True:
    temp = val % 100
    if(temp < min):
        min = temp
    val = val // 10
    if(val < 1):
        break
print(min)

#1f 
prev_digit = n % 10  # Lấy chữ số cuối cùng làm chữ số trước đó
n = n // 10  # Loại bỏ chữ số cuối cùng
flag = True
while n > 0:
    curr_digit = n % 10  # Lấy chữ số hiện tại
    if curr_digit >= prev_digit:
        flag = False
    prev_digit = curr_digit
    n = n // 10
if(flag == True):
    print("tang nghiem ngac")
else:
    print("khong tang nghiem ngac")

#2 Draw square
a = eval(input("Nhap so canh: "))
