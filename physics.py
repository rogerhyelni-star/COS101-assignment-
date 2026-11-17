def speed():
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))

    if time == 0:
        print("Time cannot be zero.")
    else:
        result = distance / time
        print("Speed =", result, "m/s")


# Function to calculate Acceleration
def acceleration():
    final_velocity = float(input("Enter final velocity (m/s): "))
    initial_velocity = float(input("Enter initial velocity (m/s): "))
    time = float(input("Enter time (s): "))

    if time == 0:
        print("Time cannot be zero.")
    else:
        result = (final_velocity - initial_velocity) / time
        print("Acceleration =", result, "m/s²")


# Function to calculate Force
def force():
    mass = float(input("Enter mass (kg): "))
    acceleration_value = float(input("Enter acceleration (m/s²): "))

    result = mass * acceleration_value
    print("Force =", result, "N")


# Function to calculate Work Done
def work():
    force_value = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))

    result = force_value * distance
    print("Work Done =", result, "J")


# Function to calculate Kinetic Energy
def kinetic_energy():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))

    result = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", result, "J")


# Main Program
while True:

    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Speed")
    print("2. Acceleration")
    print("3. Force")
    print("4. Work Done")
    print("5. Kinetic Energy")

    choice = input("\nSelect a physics operation (1-5): ")

    try:
        if choice == "1":
            speed()

        elif choice == "2":
            acceleration()

        elif choice == "3":
            force()

        elif choice == "4":
            work()

        elif choice == "5":
            kinetic_energy()

        else:
            print("Invalid selection!")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    # Ask user whether to continue
    while True:
        answer = input(
            "\nWould you like to perform another calculation? (yes/no): "
        ).lower().strip()

        if answer in ["yes", "y"]:
            break

        elif answer in ["no", "n"]:
            print("Thank you for using the Physics Calculator!")
            exit()

        else:
            print("Please enter yes or no.")
