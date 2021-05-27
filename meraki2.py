# Pre-defined Functions Questions

# Ab aapko kuchh questions solve krna hai pre-define function ka use 
# kr ke. Q1 . Aapko max function ka use krke di hue list me se sbse bada value print krvani hai. Input
 
numbers = [3, 5, 7, 34, 2, 89, 2, 5] 
max=numbers[0]
i=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i=i+1
print(max)

