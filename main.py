#Write a python script to take input for 3 numbers, and print the largest number.

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
max=0
if a>b and a>c:
    max=a
else :
     if b>c:
        max=b
     else:
        max=c
        print("largest number is", max)
#Program to display the Fibonacci sequence up to n-th term.
ntearms = int(input("how many tearms? "))
n1, n2 = 0,1
count = 0
if ntearms<= 0:
    print("please enter a positive integer")
elif ntearms == 1:
        print("Fibonacci sequence upto", ntearms,":")
        print(n1)
else:
            print("Fibonacci sequence:")
while count < ntearms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2= nth
        count += 1 


"""Write a program to print following pattern.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5"""

for i in range (1, 6) :
    for j in range (1, i+1) :
        print(j, end="")
        print()

#Write a python program using a function to print factorial of given number.

def facto() :
    n=int(input("Enter the number:"))
    f=1
    for i in range(1,n+1) :
        f*=i
    print("Factorial of " ,n, "is: ",f, end=" " )        
facto()
