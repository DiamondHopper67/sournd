for i in range(1,6):
    for e in range(1,i+1):
        print("~",end=" ")
    print()

for r in range(1,6):
    for d in range(1,r+1):
        print(d,end=",")
    print("")

for q in range(0,11):
    for w in range(0,q+1):
        print(w, end="-")
    print("")

for x in range(1,11):
    for y in range(1,11):
        print(x*y,end=" ")
    print("")

for v in range(1,6):
    for t in range(6,v,-1):
        print("~",end=" ")
    print()

for u in range(10, 1,-1):
    print(u)