x=int(input("Enter a number: "))
s=0
y=x
while x!=0:

    t=x%10
    s=s*10+t
    x=x//10

if s==y:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

