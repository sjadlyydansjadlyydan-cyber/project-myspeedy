def main():
    name = input("What's your name? ")
    print("Hello", name)

    num = int(input("Enter any number: "))
    if num > 0:
        print("That's a positive number.")
    elif num < 0:
        print("That's a negative number.")
    else:
        print("You entered zero.")

    print("Let's count up to your number:")
    for i in range(1, num + 1 if num > 0 else 6):
        print(i)

    print("Now let's do a quick sum from 1 to 5.")
    total = 0
    x = 1
    while x <= 5:
        total += x
        x += 1
    print("The total is", total)

main()
