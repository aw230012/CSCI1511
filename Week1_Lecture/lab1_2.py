SALES_TAX = .065
LICENSE_FEE = .03
TITLE_FEE = 99.95
DEALER_PREP_FEE = 1000.00
DESTINATION_FEE = 1250.00

car_price = float(input("Enter the sale price of the car: $"))
sales_tax_cost = car_price * SALES_TAX
license_fee_cost = car_price * LICENSE_FEE
total = car_price + sales_tax_cost + license_fee_cost + TITLE_FEE \
  + DEALER_PREP_FEE + DESTINATION_FEE

print(f"Car price: ${car_price:.2f}") #
print(f"Sales tax: ${sales_tax_cost:.2f}")
print(f"License fee: ${license_fee_cost:.2f}")
print(f"Title fee: ${TITLE_FEE:.2f}")
print(f"Dealer prep fee: ${DEALER_PREP_FEE:.2f}")
print(f"Destination fee: ${DESTINATION_FEE:.2f}")
print(f"Total cost: ${total:.2f}")
