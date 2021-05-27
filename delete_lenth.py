def delete_nth(list,num):
    i=0
    while i<num:
        list.pop()
        i=i+1
    print(list)
delete_nth ([20,37,20,21],1) 