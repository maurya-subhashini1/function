# Ek function likhiye jo ki ek limit naam ka parameter lega aur 0 se limit tak 
# ke beech ke number jo ki 3 aur 5 ke multiples hain unka sum print karega.
# jaisa ki niche dikhaya gya hai. Input:- 3 aur 5 ke multiples 
# => 3, 5, 6, 9, 10 Output :-

def maurya(limit):
    i=0
    s=0
    while i<10:
        a=i*3 and i*5
        s=s+a
        i=i+1
    print(s)
maurya([3,5,6,9,10])
