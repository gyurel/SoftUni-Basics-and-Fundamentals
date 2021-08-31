class Vehicle:

    owner = None

    def __init__(self, vehicle_type: str, model: str, price: int):
        self.type = vehicle_type
        self.model = model
        self.price = price

    def buy(self, money, owner):
        if money >= self.price and self.owner == None:
            self.owner = owner
            change = money - self.price
            output = f"Successfully bought a {self.type}. Change: {change:.2f}"

            return output

        elif money < self.price:
            output = f"Sorry, not enough money"

            return output

        elif self.owner != None:
            output = f"Car already sold"

            return output

    def sell(self):
        if self.owner != None:
            self.owner = None

        elif self.owner == None:
            output = f"Vehicle has no owner"

            return output

    def __repr__(self):
        if self.owner != None:
            output = f"{self.model} {self.type} is owned by: {self.owner}"

            return output

        elif self.owner == None:
            output = f"{self.model} {self.type} is on sale: {self.price}"

            return output


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
