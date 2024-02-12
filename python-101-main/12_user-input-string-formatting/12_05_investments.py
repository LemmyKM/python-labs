# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

investment_amount = int(input('enter investment amount : '))
interest_rate = float(input('enter interest rate : '))
number_of_years = int(input('enter number of years : '))

print(f"The interest amount will be {investment_amount * interest_rate/100 * number_of_years:.2f}")
