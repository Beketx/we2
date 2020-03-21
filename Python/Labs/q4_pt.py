a = int(input())
a = a % 1440
x = a // 60
y = a % 60 #3600 60
if x < 10:
	x = '0{}'.format(x)
elif x > 24:
	x = x % 24
if y < 10:
	y = '0{}'.format(y)
print('{}:{}'.format(x,y))