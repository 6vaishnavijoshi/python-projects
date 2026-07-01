# ===============================
# Unit Converter
# ===============================

def temperature_converter():

    print("\n------ Temperature Converter ------")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice: ")

    if choice == "1":

        celsius = float(input("Enter Temperature in Celsius: "))

        fahrenheit = (celsius * 9 / 5) + 32

        print(f"Result: {fahrenheit:.2f} °F")

    elif choice == "2":

        fahrenheit = float(input("Enter Temperature in Fahrenheit: "))

        celsius = (fahrenheit - 32) * 5 / 9

        print(f"Result: {celsius:.2f} °C")

    else:

        print("Invalid Choice!")


def length_converter():

    print("\n------ Length Converter ------")
    print("1. Kilometer to Meter")
    print("2. Meter to Kilometer")
    print("3. Meter to Centimeter")
    print("4. Centimeter to Meter")

    choice = input("Enter your choice: ")

    if choice == "1":

        km = float(input("Enter Kilometer: "))

        meter = km * 1000

        print(f"Result: {meter:.2f} m")

    elif choice == "2":

        meter = float(input("Enter Meter: "))

        km = meter / 1000

        print(f"Result: {km:.2f} km")

    elif choice == "3":

        meter = float(input("Enter Meter: "))

        cm = meter * 100

        print(f"Result: {cm:.2f} cm")

    elif choice == "4":

        cm = float(input("Enter Centimeter: "))

        meter = cm / 100

        print(f"Result: {meter:.2f} m")

    else:

        print("Invalid Choice!")


def weight_converter():

    print("\n------ Weight Converter ------")
    print("1. Kilogram to Gram")
    print("2. Gram to Kilogram")

    choice = input("Enter your choice: ")

    if choice == "1":

        kg = float(input("Enter Kilogram: "))

        gram = kg * 1000

        print(f"Result: {gram:.2f} g")

    elif choice == "2":

        gram = float(input("Enter Gram: "))

        kg = gram / 1000

        print(f"Result: {kg:.2f} kg")

    else:

        print("Invalid Choice!")


def volume_converter():

    print("\n------ Volume Converter ------")
    print("1. Liter to Milliliter")
    print("2. Milliliter to Liter")

    choice = input("Enter your choice: ")

    if choice == "1":

        liter = float(input("Enter Liter: "))

        ml = liter * 1000

        print(f"Result: {ml:.2f} mL")

    elif choice == "2":

        ml = float(input("Enter Milliliter: "))

        liter = ml / 1000

        print(f"Result: {liter:.2f} L")

    else:

        print("Invalid Choice!")


# ===============================
# Main Program
# ===============================

while True:

    print("\n===================================")
    print("       UNIT CONVERTER")
    print("===================================")
    print("1. Temperature Converter")
    print("2. Length Converter")
    print("3. Weight Converter")
    print("4. Volume Converter")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":

        temperature_converter()

    elif choice == "2":

        length_converter()

    elif choice == "3":

        weight_converter()

    elif choice == "4":

        volume_converter()

    elif choice == "5":

        print("\nThank You for Using Unit Converter!")
        break

    else:

        print("\nInvalid Choice! Please Enter Between 1 and 5.")