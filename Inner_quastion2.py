# Ek perfect() naam ka function define kijiye jo ki ek parameter lega aur uss
#  parameter ko hume check karana hai ki vo perfect number hain ya nahi.
#   Iske baad uss function ko use karke ek program likhiye jo ki 1 se 1000 
#   tak sabhi perfect numbers ko print kare.[ hum ek aise integer number ko
#    perfect number kahenge jo ki uske sabhi factors ( including 1 & excluding 
#    itself) ka sum uss number ke barabar hota hai. Example:- Expected Output :- 


def perfect(num):
    i=1
    a=0
    while i<num:
        if(num%i)==0:
            a=a+i
        i=i+1
    if a==num:
        print("is perfect number") 
    else:
        print(num,"is not perfect number")
num=int(input("enter the number"))
perfect(num)     
        

 