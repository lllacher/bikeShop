from bicycles import *

def create_initial_inventory():
    """ create 6 bike objects for initial inventory list """
    bike1 = Bicycle("Shimano", 12, 3, 270)
    bike2 = Bicycle("Mobo", 35, 5, 300)
    bike3 = Bicycle("Swiss Army", 25, 1, 800)
    bike4 = Bicycle("Hollandia", 20, 4, 225)
    bike5 = Bicycle("Ozone", 20, 6, 70)
    bike6 = Bicycle("Schwinn", 22, 5, 150)

    return [bike1,bike2,bike3,bike4,bike5,bike6]
   
def create_initial_customers():
    """ create 3 customers objects for initial customer list """
    customer1 = Customer("Mark", 500)
    customer2 = Customer("Kyle", 1000)
    customer3 = Customer("Quinn", 200)

    return [customer1, customer2, customer3]

def main():
    # setup
    inventory = create_initial_inventory()  # create initial bike inventory list
    shop = Bike_Shop("Academy", inventory)  # create bike shop
    customers = create_initial_customers()  # create initial customer list

    # display bike inventory for shop
    shop.display_inventory()

    # make bike recommendations for each customer and ask them to purchase
    for customer in customers:
        print("Hello {}, welcome to {}.".format(customer.name, shop.name))
        print("Based on your budget of ${}, we recommend the following bikes:".format(customer.budget))
        # display bike recommendations for each customer based on customer budget
        bike_list = shop.get_recommendation(customer.budget)
        if bike_list == []:
            print("I am sorry, but we have no bikes that meet your budget")
        else:
            for bike in bike_list:
                print("Model:", format(bike[0], '<15s'),"Price: ",format(bike[1], ',.2f'))
        print()
        
        # help customer purchase a bike
        model = input("Please enter the model number of the bike you would like to purchase. Enter NA, if you do not wish to purchase a bike at this time. ")
        if model.upper() == "NA":
            print()
            print("Please consider us when you are ready to purchase a bike.")
            print()
        else:
            successful_transaction, response, price, remaining_budget = shop.purchase_bike(model, customer)
            if successful_transaction:
                print()
                print(response)
                print("The bike cost ${} and you have ${} remaining in your bike budget.".format(format(price, ',.2f'), format(remaining_budget, ',.2f')))
                print()
            else:
                print(response, "Your remaining budget is {}.".format(format(remaining_budget, ',.2f')))
                print()
    
    # after all bikes purchased, print remaining inventory and total profit made
    shop.display_inventory()
    print("Total profits: ${}.".format(format(shop.profit, ',.2f')))
    
main()

