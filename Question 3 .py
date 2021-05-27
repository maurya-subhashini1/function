# add_numbers_list naam ka function likhiye jo do integers ki 
# 2 lists leta ho aur fir same position wale integers ka sum print karta ho.
#  Same position waale 2 integers ka sum karne ke liye Part 
#  1 mein di gayi add_numbers waale function ka use karo. 
#  Jaise agar hum iss function ko[50, 60, 10] aur [10, 20, 13]
#   denge ko woh yeh print karega


def add_numbers_list(x,y):
    i=0
    j=0
    d=[]
    while i<len(x):
        while j<len(y):
            s=x[i]+y[j]
            d.append(s)
            break
        j=j+1
        i=i+1
    print(d)
a=[50, 60, 10]
b=[10, 20, 13]
add_numbers_list(a,b)

