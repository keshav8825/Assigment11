#7. Write a python script to count digits in a given number
'''n=input("Enter a number:-")
l=len(n)
print(l)
print()'''

n=int(input("enter a number:-"))
count=0
while n!=0:
    n=n//10
    count+=1
print(count)
print()
