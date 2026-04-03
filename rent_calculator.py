# Rent Calculator
'''
# Inputs:
1. Total rent
2. Total food ordered for snacking
3. Electricity units spend
4. Charge per Unit
5. Persons living in room/flat

# Output:
1. Total amount to pay
'''
# Input part: taking necessary inputs from the users.
rent = int(input("Enter your rent: "))
food = int(input("Enter the amount of food ordered: "))
electricity_spend = int(input("Enter the total of electricity spend: "))
charge_per_unit = int(input("Enter the charge per unit: "))
total_person = int(input("Enter the number of persons living in the flat/ room: "))

### Logic starts ###
# total electricity spend
total_electricity_bill = electricity_spend * charge_per_unit

# Total amount per person have to pay
pay_per_person = (rent + food + total_electricity_bill) // total_person

# Output
print(f"we have {total_person} persons living in the flat/room. So we have to pay total sum of {pay_per_person}")
