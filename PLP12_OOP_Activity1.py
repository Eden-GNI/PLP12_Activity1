#!/usr/bin/python3

class Passenger:
    def __init__(self, name, location, destination, date):
        self.name = name
        self.location = location
        self.destination = destination
        self.date = date

    def get_passenger_info(self):
        return (
            f"Name: {self.name}\n"
            f"From: {self.location}\n"
            f"To: {self.destination}\n"
            f"Date: {self.date}\n"
            f"Weight allowance: {self.get_weight_allowance()} kg"
        )

    def get_weight_allowance(self):
        return 20

    def common_method(self):
        return f"Common action: (self.name)"

class Economy(Passenger):
    def __init__(self, name, location, destination, date, seat_preference):
        super().__init__(name, location, destination, date)
        self.seat_preference = seat_preference

    def get_passenger_info(self):
        return super().get_passenger_info() + f"\nSeat preference: {self.seat_preference}"

class Business(Passenger):
    def __init__(self, name, location, destination, date, lounge_pass_code):
        super().__init__(name, location, destination, date)
        self.lounge_pass_code = lounge_pass_code

    def get_weight_allowance(self):
        return 100

    def get_passenger_info(self):
        return super().get_passenger_info() + f"\nLounge pass code: {self.lounge_pass_code}"

    def get_business_details(self):

    while True:
        code = input("Lounge pass code: ").strip()
        if code:
            return code
        print(" Error: this field cannot be empty. Please try again.")

class First_Class(Passenger):
    def __init__(self, name, location, destination, date, suite_number, chauffeur_service):
        super().__init__(name, location, destination, date)
        self.suite_number = suite_number
        self.chauffeur_service = chauffeur_service

    def get_passenger_info(self):
        return (
            super().get_passenger_info()
            + f"\nSuite number: {self.suite_number}"
            + f"\nChauffeur service: {self.chauffeur_service}"
        )

    def specific_method(self):
        return f"Specific action: (self.menu)"

#Add the prompt code here





#Add economy code here






#Add FIrst class Code here


def dynamic_data_entry():
    print("\n===== AIRLINE TICKET BOOKING =====")
    print("1. Economy Class")
    print("2. Business Class")
    print("3. First Class")

    while True:
        choice = input("Select ticket class (1-3): ").strip()
        if choice in ["1", "2", "3"]:
            break
        print("Invalid choice. Please select 1, 2, or 3.")

    print("\n===== PASSENGER DETAILS =====")

    name = input("Enter passenger name: ").strip()
    location = input("Enter departure location: ").strip()
    destination = input("Enter destination: ").strip()
    date = input("Enter travel date: ").strip()

    if choice == "1":
        seat = input("Enter seat preference: ")
        passenger = Economy(name, location, destination, date, seat)

    elif choice == "2":
        lounge_code = input("Enter lounge pass code: ")
        passenger = Business(name, location, destination, date, lounge_code)

    else:
        suite = input("Enter suite number: ")
        chauffeur = input("Require chauffeur service? (Yes/No): ").strip().lower()

        passenger = First_Class(
            name, location, destination, date,
            suite, chauffeur == "yes"
        )

    print("\n===== BOOKING SUMMARY =====")
    print(passenger.get_passenger_info())

    return passenger


if __name__ == "__main__":
    dynamic_data_entry()
