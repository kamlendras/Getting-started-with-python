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
