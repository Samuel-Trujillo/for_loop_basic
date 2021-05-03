for i in range(0,151):
    print(i)

for x in range(5,1001,5):
    print(x)

for z in range(1,101):
    if z%10 == 0:
        print("Coding Dojo")
    elif z%5 == 0:
        print("Coding")
    else:
        print(z)

sum = 0
for s in range(0,500001,1):
    if s%2 != 0:
        sum= sum+ s 
print(sum)

for p in range(2018,0,-4):
    print(p)

lownum= 10
highnum= 100
mult= 5
for d in range(lownum,highnum+1):
    if d % mult ==0:
        print(d)
