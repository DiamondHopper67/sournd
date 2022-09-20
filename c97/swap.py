f1= input("enter file 1")
f2= input("enter file 2")

a= open(f1,"r")
data1=a.read()

b=open(f2,"r")
data2=b.read()

c=open(f1,'w')
c.write(data2)

d=open(f2,"w")
d.write(data1)