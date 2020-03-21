spisok = [int(i) for i in input().split()]
spisok2 = spisok[::2]
print(*spisok2)

spisok = [int(i) for i in input().split()]
spisok2 = filter(lambda x: x%2==0, spisok)
print(*spisok2)

spisok = [int(i) for i in input().split()]
spisok2 = filter(lambda x: x>0, spisok)
print(len(list(spisok2)))
