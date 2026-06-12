print("UNIT CONVERTER")
print("1. Kilometer to Meter")
print("2. Kilogram to Gram")
print("3. Celsius to Fahrenheit")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        km = float(input("Enter kilometer: "))
        meter = km * 1000
        print("Meter =", meter)
    elif choice == 2:
        kg = float(input("Enter kilogram: "))
        gram = kg * 1000
        print("Gram =", gram)
    elif choice == 3:
        c = float(input("Enter Celsius: "))
        f = (c * 9/5) + 32
        print("Fahrenheit =", f)
    else:
        print("Invalid Choice")
    again = input("Meedum convert pannava? (yes/no): ")
    if again == "no":
        print("Bye!")
        break