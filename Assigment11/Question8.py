#8. Write a python script to calculate sum of digits of a given number
n=int(input("enter any number"))
s=0
while n>0:
    rem=n%10
    s=s+rem
    n=n//10
print("sum is",s)
print()
    
