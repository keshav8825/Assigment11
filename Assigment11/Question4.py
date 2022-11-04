#4. Write a python script to calculate sum of first N odd natural numbers
n=int(input("enter a number:-"))
s=0
i=1
while i<=n:
    s=s+(2*i-1)
    i+=1
print("sum of odd natural number is",s)
print()    
  
    
