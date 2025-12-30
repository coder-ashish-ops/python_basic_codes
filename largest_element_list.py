l = []
n = int(input("Enter number: "))

for i in range(n):
    x =  int(input())
    l.append(x)


max = l[0]
for i in l:
    if(i > max):
        max =i

print(max)