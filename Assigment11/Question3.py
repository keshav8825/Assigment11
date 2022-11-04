#3. Write a python script to calculate sum of cubes of first N natural numbers
n=int(input("Enter any number"))
s=0
i=1
while i<=n:
    s=s+(i*i*i)
    i+=1
print("sum of cube is ",s)
print()
    
