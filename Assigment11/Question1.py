#1. Write a python script to calculate sum of first N natural numbers

n=int(input("Enter a number:-"))
s=0
i=1
while i<=n:
    s=s+i
    i+=1
print("sum is",s)
print()    
