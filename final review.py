'''
mylist = [[2,4,1],[1,2,3],[2,3,5]]
a=0
b=0
total=0
while a<=2:
    while b < 2:
        total += mylist[a][b]
        b += 1
    a+=1
    b=0
print(total)

for fruit in ["banana", "apple", "quince"]:
    print (fruit)
    
i = 2

def myf(s, n):
    global i
    print(s * i * n)

myf('hi-', 3)
'''
mylist = [[2,2,1],[1,2,3],[1,1,1]]
total = 0
for sublist in mylist:
    total += sum(sublist)
print(total)
