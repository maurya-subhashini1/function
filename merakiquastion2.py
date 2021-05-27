# def add_numbers(num1,num2) :
#     sum=num1+num2
#     print(sum)
# add_numbers(56,12)


def check_numbers_list(x,y):
    i=0
    j=0
    while i<len(x):
        while j<len(y):
            if x[i]%2==0 and y[j]%2==0: 
                print("both are  even number")
            else:
                print("not even number")
            j=j+1
            i=i+1
a=[2, 6, 18, 10, 3, 75]
b=[6, 19, 24, 12, 3, 87] 
check_numbers_list(a,b)
                    