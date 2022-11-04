#2. Write a python script to calculate sum of squares of first N natural numbers
n=int(input("Enter any number:-"))
s=0
i=1
while i<=n:
    s=s+(i*i)
    i+=1
print("sum of square is",s)
print()    
