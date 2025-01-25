## This program adds up the cost of meals and drinks for children and adults, 
# adds the sales tax, and shows the change from the payment.

price_of_child_meal = float(input("What is the price of a child's meal? "))

price_of_adult_meal = float(input("What is the price of an adult's meal? "))

price_of_child_drink = float(input("What is the price of a child's drink? "))

price_of_adult_drink = float(input("What is the price of an adult's drink? "))

number_of_children = int(input("How many children are there? "))

number_of_adults = int(input("How many adults are there? "))
print()

# Calculate the total price of meal and drinks for both children and adults
children_total_price = (number_of_children * price_of_child_meal) + (number_of_children * price_of_child_drink)

adult_total_price = (number_of_adults * price_of_adult_meal) + (number_of_adults * price_of_adult_drink)

# Subtotal before tax
subtotal = children_total_price + adult_total_price
print(f"Subtotal: ${subtotal:.2f}")
print()


sales_tax_rate = float(input("What is the sales tax rate? "))



sales_tax = subtotal * (sales_tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")

# Total amount after including sales tax
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")
print()


# calculation of Payment and change 
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total
print(f"Change: ${change:.2f}")
