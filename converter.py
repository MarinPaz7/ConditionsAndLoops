print("Hi!! This programme is a unit converter that converts kilometers into miles.")

while True:
    print("Please enter kilometers that you'd like to convert into miles.")

    km = input("Km:")

    km = float(km.replace(",", "."))

    miles = km * 0.621371192

    print("{0} kilometers is {1} miles.".format(km, miles))

    choice = input("Would you like to do another conversion (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        break