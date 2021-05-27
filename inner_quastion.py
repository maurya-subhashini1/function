# Ek function banaiye jo 3 numbers ka sum aur average print kare.
# Hum user se 3 number input karwayenge aur fir unn 3 numbers ka sum 
# aur average print karwayenge jaisa ki niche output diya hua hain.

def num(x,y,z):
        sum=x+y+z
        avg=sum/3
        print("sum is",sum)
        print("average is",avg)
    
x=int(input("enter the number"))
y=int(input("enter the number"))
z=int(input("enter the number"))
num(x,y,z)