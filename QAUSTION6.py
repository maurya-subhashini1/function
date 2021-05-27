def caculater(x,y):
    i=0
    j=0
    d=[]
    while i<len(x):
        while j<len(y):
            s=x[i]*y[j]
            d.append(s)
            break
        j=j+1
        i=i+1
    print(d)
a=[5, 10, 50, 20]
b=[2, 20, 3, 5]
caculater(a,b)
