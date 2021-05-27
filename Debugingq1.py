# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number") 
# isEven()



# def Convert(lst):
#     res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
#     return res_dct
# lst = ['a', 1, 'b', 2, 'c', 3]
# print(Convert(lst))


lst = [1,2,3,4,5,6,7,8]
s={}
for i in range(0,len(lst),2):
    s.update({lst[i]:lst[i+1]})
print(s)
