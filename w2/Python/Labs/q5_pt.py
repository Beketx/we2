a = int(input())
b = int(input())
l = int(input())
n = int(input())
if n != 1:
	n = n*2
	a = a*(n-2) + a
	z = b*(n/2-1)*2 + a + l*2
elif n == 1:
	n = n*2
	z = a + l*2

print(z)
