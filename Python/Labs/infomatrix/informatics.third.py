a = input("Enter a: ")
b = input("Enter b: ")
 
s = ''
 
while a<=b:
    if a%2==0: s = s + str(a)+" "
    a += 1
 
print s