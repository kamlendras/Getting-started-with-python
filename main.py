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


"""Write a python program to accept the username "Admin" as the
default argument and password 123 entered by the user to allow
login into the system."""

def user_pass (passward,username="Admin"):
    if passward=='123':
       print("You have logged into system")
    else:
         print("Password is incorrect!!!!")
password=input("Enter the password:")
user_pass(password)


"""Write a python program to demonstrate the concept of variable
length argument to calculate the product and addition of given
number."""

def add (*n) :
    total=0
    for i in n:
        total=total + i
    print ("Addition of given numbers", total)

def product (*n) :
    p=1
    for i in n:
        p = p*i
    print ("Product of given numbers:",p)
     
add(3,6,8,2,4)
product(3,6,8,2)

"""Write a python program to read a file named “article.txt”, count
and print total alphabets in the file."""

def count_alpha():
    L=0
    with open ("article.txt") as f:
        while True:
            c=f.read(1)
            if not c:
                break
            print (c,end='')
            if((c>'A' and c<= 'Z') or (c>='a' and c<='z')):
                L = L+1
                print ("total lower case alphabats ",L)
count_alpha() 




"""Write a python program to read a file named “info.txt”, count
and print total words starting with “t” or “T” in the file.
File Content:

 Python is super and trending language
 A text file stores textual data.
 Binary files can handle binary data.
 CSV files can handle tabular data.
 """
 
def count_words () :
    w=0
    with open ("info.txt") as f:
        for line in f:
            for word in line.split () :
               if(word[0]=="t" or word[0]=="T") :
                print(word)
                w=w+1
        print ("total words statting with 't' are", w)                
count_words ()     


"""
Write a program to count a total number of lines and count the
total number of lines starting with 'A', 'B', and 'C' from the file
article.txt.
File Content:

Python is a super and treanding language.
Allows to store the output in the files.
A text file stores textual data.
Binary files can handle binary data.
Binary files use pickle module to store data.
CSV files allows to handle tabular data.
CSV files can be read easily using CSV reader object.
"""
def program5() :
    with open ("article.txt", "r") as f1:
        data=f1.readlines()
        count_lines=0
        count_A=0
        count_B=0
        count_C=0
        for lines in data:
            count_lines+=1
            if lines [0] =='A':
                count_A+=1
            if lines[0] =='B':
                count_B+=1
            if lines[0] =='C':
                count_C+=1
        print("Total Number of lines are:",count_lines)
        print("Total Number of lines strating with A are:",count_A)
        print("Total Number of lines strating with B are:",count_B)
        print("Total Number of lines strating with C are:",count_C)
program5()        
        
