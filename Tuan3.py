s="Dai Hoc COng Nghe Sai Gon"

#slice
s1 = s[:4] + 'X' + s[:5]
print(s1)

print(s.lower())

print(s.upper())

x ='Dai'
y='MAX'
#replace value of y for value of x in s  
print(s.replace(x,y))
#Count character o
print(s.count('o'))
#Location of first character o
print(s.index('o'))
#Check alphabet (a-z)
text = 'Company'
flag = text.isalpha()
print(flag)

#Example Input a string if have character a print location a
s2 = input("Enter a String: ")
for i in range(len(s2)):
    if s2[i]=='a' :
        print(i,end="\t")
#Example 2
s3 =input("Enter a string: ")
print(len(s3))