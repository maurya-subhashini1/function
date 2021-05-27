# Question 7

# Ek function define karo jo ki input me 2 strings lega aur 
# dono strings me se jiski length jyaada hogi use print karega 
# aur agar dono strings ki length equal hui to dono ko line by line print karega . 
# Hint :- use len() builtin function.. Inpu


def subhashini_maurya(List):
    a=0
    i=0
    while i<len(List):
        if a<len(List[i]):
            a=len(List[i])
            c=List[i]
        i=i+1   
    print(c)
subhashini_maurya(["Swati", "Muskan","golu", "Priyanka","Madu","subhashinimaurya"])

    