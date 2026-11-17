#!/usr/bin/python3

class Passenger:
    def __init__(self, name, location, destination, date):
        self.name = name
        self.location = location
        self.destination = destination
        self.date = date

    def get_weight_allowance(self):
        return 20

    def common_method(self):
        return f"Common action: (self.name)"

class Economy(Passenger):
    def __init__(self, name, location, destination, date, seat_preference):
        super().__init__(name, location, destination, date)
        self.seat_preference = self.seat_preference

class Business(Passenger):
    def __init__(self, name, location, destination, date, lounge_pass_code):
        super().__init__(name, location, destination, date)
        self.lounge_pass_code = self.lounge_pass_code

    def get_weight_allowance(self):
        return 100

    def specific_method(self):
        return f"Specific action: (self.seat)"

class First_Class(Passenger):
    def __init__(self, name, location, destination, date, suite_number, chauffeur_service):
        super().__init__(name, location, destination, date)
        self.suite_number = suite_number
        self.chauffeur_service

    def specific_method(self):
        return f"Specific action: (self.menu)"
