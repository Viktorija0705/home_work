class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand= brand
        self.passangers = []

    def add_passanger(self,human):
        self.passangers.append(human)

    def pint_number_of_passangers(self):
        if len(self.passangers) == 0:
            print(f"There are zero {self.brand} passangers")

        else:
            print(f"There are {len(self.passangers)} passangers in {self.brand}")
            for passanger in self.passangers:
                print(passanger.name)

nick = Human("One")
kate = Human("Two")
car= Auto("Mercedes")
car.add_passanger(nick)
car.add_passanger(kate)
car.pint_number_of_passangers()