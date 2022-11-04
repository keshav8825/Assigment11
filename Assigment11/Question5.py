#5. Write a python script to calculate sum of first N even natural numbers
n=int(input("enter any number:-"))
s=0
i=1
while i<=n:
    s=s+(2*i)
    i+=1
print("sum of first n even natural number",s)    
print()
