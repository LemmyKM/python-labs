print()
km = float(input('trip distance in km: '))
car_consumption_lit_per_100kilometer = float(input('liters per 100 kilometer cons. of the car : '))
price_liter = float(input('price per liter fuel : '))

print(f"The cost of the trip will be R{km * (car_consumption_lit_per_100kilometer/100) * price_liter:.2f}")