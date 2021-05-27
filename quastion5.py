# check_numbers naam ka ek function likhiye jo do numbers le aur fir print kare "Dono even hain" agar dono numbers even (2 se divide hote hain) nahi toh print kare
#  "Dono numbers even nahi hai"



def check_numbers(x,y):
    if x%2==0:
        if y%2==0:
           print("x and y both are even number")
        else:
            print("x is  even")
    else:
        print("x is not even number")
x=int(input("enter the number"))
y=int(input("enter the number"))
check_numbers(x,y)