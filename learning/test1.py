n =int(input("Enter an integer:"))
if n % 2 != 0:
    print("Weird")
elif n in range(2, 6):
    print("Not Weird")
elif n in range(6, 21):
    print("Weird")
elif n in range(21,101):
    print("Not Weird")