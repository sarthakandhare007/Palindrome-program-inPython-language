n = int(input("Enter an integer: "))

if n < 0:
    print("Not a palindrome")
else:
    original = n
    rev = 0
    x = n
    while x > 0:
        rev = rev * 10 + (x % 10)
        x //= 10

    if rev == original:
        print("Palindrome")
    else:
        print("Not a palindrome")
