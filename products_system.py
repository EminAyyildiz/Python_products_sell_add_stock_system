# Written by Emin Ayyıldız
print("Written by EMİN AYYILDIZ")
import time
from enum import Enum

class PaymentMethod(Enum):
    CREDIT_CARD = 1
    PAYPAL = 2
    CASH = 3

def add_products():
    product_serial_number = input("Enter product serial number : ")
    product_name = input("Enter product name : ")
    product_price = float(input("Enter product price: "))
    stock = int(input("Enter product stock: "))
    products[product_serial_number] = {"product_name": product_name, "product_price": product_price, "stock": stock}
    print(product_name, "has been added to the inventory.")

def update_products():
    product_serial_number = input("Enter product serial number : ")
    if product_serial_number in products:
        product_price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        products[product_serial_number]["product_price"] = product_price
        products[product_serial_number]["stock"] = stock
        print("Information is being updated, please wait....")
        time.sleep(1.5)
        print("Product information has been updated...")
    else:
        print("Product not found")

def sell_product():
    product_serial_number = input("Enter product serial number : ")
    if product_serial_number in products:
        sell_amount = int(input("How many products will be sold : "))
        if products[product_serial_number]["stock"] >= sell_amount:
            total_price = products[product_serial_number]["product_price" ] *sell_amount
            print("Total price for", sell_amount, products[product_serial_number]["product_name"], "is:", total_price)
            print("Select payment method : ")
            for payment_method in PaymentMethod:
                print(payment_method.value, payment_method.name)

            selected_payment_method = int(input("--->"))
            if selected_payment_method == PaymentMethod.CREDIT_CARD.value:
                card_number = input("Enter your 16 digit card number : ")
                card_password = input("Enter your 4 digit card password  : ")
                if len(card_number) >= 15 and len(card_password) == 4:
                    print("Payment is progress, please wait...")
                    time.sleep(1.5)
                    print("Credit card payment processed.")
                    products[product_serial_number]["stock"] -= sell_amount
                    print(sell_amount, products[product_serial_number]["product_name"], "has been sold.")
                else:
                    print("Invalid card number...")
            elif selected_payment_method == PaymentMethod.PAYPAL.value:
                paypal_card_number = input("Enter your 16 digit card number : ")
                paypal_card_password = input("Enter your 4 digit card password  : ")
                if len(paypal_card_number) >= 15 and len(paypal_card_password) == 4:
                    print("Payment is progress, please wait...")
                    time.sleep(1.5)
                    print("Paypal payment processed.")
                    products[product_serial_number]["stock"] -= sell_amount
                    print(sell_amount, products[product_serial_number]["product_name"], "has been sold.")
                else:
                    print("Invalid card number...")

            elif selected_payment_method == PaymentMethod.CASH.value:
                print("Cash payment processed.")
                products[product_serial_number]["stock"] -= sell_amount
                print(sell_amount, products[product_serial_number]["product_name"], "has been sold.")
            else:
                print("Invalid payment method.")

        else:
            print("Sorry, the stock for", products[product_serial_number]["product_name"], "is not enough.")

products = {}

def display_all_products():
    for product_serial_number, product_info in products.items():
        print("All products are listed please wait...")
        time.sleep(2)
        print("Product ID:", product_serial_number)
        print("Name:", product_info["product_name"])
        print("Price:", product_info["product_price"])
        print("Stock:", product_info["stock"])
        print("----------------")

def check_admin_credentials(username, password):
    if username == "admin" and password == "1234":
        print("Logging into account, please wait...")
        time.sleep(2)
        print("Login to the system.")
        return True
    else:
        print("Wrong username or password...")
        return False

while True:
    print("Welcome to the system of our store. We wish you a nice day..")
    username = input("Please enter username :")
    password = input("Please enter password : ")
    if check_admin_credentials(username, password):
        while True:
            print \
                ("***MENU*** \n1- Add Products \n2- Update Products \n3- Sell Products \n4- Display All Products \n5- EXIT")
            choice = int(input("Please enter your choice : "))
            if choice == 1:
                add_products()
            elif choice == 2:
                update_products()
            elif choice == 3:
                sell_product()
            elif choice == 4:
                display_all_products()
            elif choice == 5:
                break
            else:
                print("Invalid chosen...")

