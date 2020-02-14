
n = int(input("enter rows"))
m = int(input("enter colums"))
a=[]
b=[]
c=[]
for i in range(n):
    for j in range(m):
        x = int(input("enter values"))
        a.append(x)
        b.append(a)
        a=[]

        for i in range(n):
            x =int(input("enter values"))
            a.append(x)
            c.append(a)
            a=[]

             for i in range(n):
                 for j in range(m):
                     print(b[i][j]+c[i][j])