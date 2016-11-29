class Bicycle:
    def __init__(self, model, weight, qty, cost):
        self.model = model
        self.weight = weight
        self.qty = qty
        self.cost = cost

class Bike_Shop:
    def __init__(self, name, inventory, margin = 20):
        self.name = name
        self.inventory = inventory
        self.margin = margin/100+1
        self.profit = 0

    def display_inventory(self):
        print("   Current Inventory")
        count = 0
        for bike in self.inventory:
            if bike.qty > 0:
                print("Model:", format(bike.model, '<15s'),"Qty: ",bike.qty)
                count += 1
        if count == 0:
            print("I am sorry, but we are all sold out of bikes!")
        print()
        
    def get_recommendation(self, budget):
        bike_list = []
        for bike in self.inventory:
            price = bike.cost*self.margin
            if price <= budget:
                bike_list.append((bike.model, price))
        return bike_list

    def purchase_bike(self, model, customer):
        for bike in self.inventory:
            if bike.model.upper() == model.upper():
                if bike.qty > 0:
                    price = bike.cost*self.margin
                    if customer.budget >= price:
                        bike.qty -= 1
                        customer.budget -= price
                        self.profit += price-bike.cost
                        return (True, "Thankyou for your purchase of a {}!".format(model), price, customer.budget)
                    else:
                        return (False, "You did not have sufficient funds in your bike budget for the {}.".format(model), price, customer.budget)
                else:
                    return (False, "We are sorry, but we do not have enough of the {} bikes in stock.".format(model), price, customer.budget)

class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        
