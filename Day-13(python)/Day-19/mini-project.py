# Personal Information Collector

# Taking input from user
name = input("Enter full name: ")
age = input("Enter age: ")
gender = input("Enter gender: ")
city = input("Enter city: ")
state = input("Enter state: ")
country = input("Enter country: ")
email = input("Enter email: ")
phone = input("Enter phone number: ")

# Printing formatted output
print("\n" + "=" * 55)
print("        PERSONAL INFORMATION CARD")
print("=" * 55)

print("Full Name     :", name)
print("Age           :", age)
print("Gender        :", gender)
print("City          :", city)
print("State         :", state)
print("Country       :", country)
print("Email         :", email)
print("Phone Number  :", phone)
print("=" * 55)



# Simple Billing System
# Taking input
customer_name = input("Customer name: ")

item1 = input("Item 1 name: ")
price1 = float(input("Item 1 price: "))

item2 = input("Item 2 name: ")
price2 = float(input("Item 2 price: "))

item3 = input("Item 3 name: ")
price3 = float(input("Item 3 price: "))

# Calculations
total_amount = price1 + price2 + price3
gst = total_amount * 0.05
final_amount = total_amount + gst

# Output
print("\n" + "=" * 55)
print("                  BILL RECEIPT")
print("=" * 55)
print("Customer Name :", customer_name)
print("-" * 40)

print("Item            Price(Rs.)")
print(item1.ljust(15), price1)
print(item2.ljust(15), price2)
print(item3.ljust(15), price3)
print("-" * 40)
print("Total Amount :", total_amount)
print("GST (5%)     :", gst)
print("Final Amount :", final_amount)
print("=" * 55)

