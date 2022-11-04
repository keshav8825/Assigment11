'''9. Write a python script to print binary equivalent of a given decimal number. (do not
use bin() method)'''
n=int(input("enter anumber"))
s=''
while n:
    s=str(n%2)+s
    n=n//2

print(s)
print()
    
