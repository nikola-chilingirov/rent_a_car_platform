cars = [
    {"id": 1, "brand": "Toyota", "model": "Corolla", "rental_price": 30, "availability": True},
    {"id": 2, "brand": "Honda", "model": "Civic", "rental_price": 35, "availability": True},
    {"id": 3, "brand": "Ford", "model": "Focus", "rental_price": 25, "availability": True}
]


# Речник за проследяване на статуса на наемане
rental_status = {}
# Функция за наемане на кола


def rent_car(car_id, user):
    for car in cars:
        if car["id"] == car_id and car["availability"]:
            car["availability"] = False
            rental_status[user] = {"car_id": car_id, "rental_price": car["rental_price"], "rental_duration": 0}
            print(f"Car {car['brand']} {car['model']} rented successfully!")
            return
    print("Car not available or invalid car ID.")
# Функция за връщане на кола


def return_car(user, rental_duration):
    if user in rental_status:
        car_id = rental_status[user]["car_id"]
        rental_price = rental_status[user]["rental_price"]
        total_cost = rental_price * rental_duration
        for car in cars:
            if car["id"] == car_id:
                car["availability"] = True
                break
        del rental_status[user]
        print(f"Car returned successfully! Total cost: ${total_cost}")
    else:
        print("No car rented by this user.")
# Функция за показване на наличните коли


def view_available_cars():
    print("Available cars:")
    for car in cars:
        if car["availability"]:
            print(
                f"ID: {car['id']}, Brand: {car['brand']}, Model: {car['model']}, Rental Price: ${car['rental_price']} per day")


#view_available_cars()


def returning_car(): #  function to return the car
    user_name = input("\nPlease, enter your names: ") # Prompt the user to enter his names.
    duration_of_rent = int(input("Please, enter duration of the rent. Keep in mind, that the price is per day.\n"
                                 "If the day has started, the whole day is considered: ")) # Prompt the user to enter duration of the rent.
    if user_name in rental_status:  # Check if the user is in dictionary for rentals.
        return_car(user_name, duration_of_rent) # calling function to return the car


def renting_car(): # function to rent the car
    while True: # Loop that let user to input id again if chosen one is not available
        choice = int(input("\nChoose id of car you want to rent: "))
        for car in cars:
            if car["id"] == choice and car["availability"]: # Check if chosen car is available, if it is, prompt user to input names, if not, prompt you for new input
                name_user = input("\nPlease, enter your names. ")
                return rent_car(choice, name_user) # calling function to rent the car
        print("Car not available or invalid car ID.\nPlease, try again.")


def display_cars(): # function to display available cars
    print("\nAvailable Cars:")
    view_available_cars() # calling function to display available cars


def main_menu():
    """Display the main menu."""
    print("\nWelcome to RentACar")
    print("1. View Car")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Exit")
    return int(input("Please choose an option (1-4): "))


def main():
    """Main function to run the platform."""
    while True: # validation to ensure the user enters valid options
        choice = main_menu()  # Display the menu and get user choice

        # Process user input based on their choice
        if choice == 1:
            display_cars() # calling function to display available cars
        elif choice == 2:
            renting_car() # Prompt the user to choose id of car and insert his names. Checking if the chosen car is available. If available calling function to rent the car.
        elif choice == 3:
            returning_car() # Prompt the user to enter his names and duration of the rent.
        elif choice == 4:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.") # if the user enter invalid option, receive error message and return for new input


main()
