# Fahrenheit to Celsius:
# ----------------------
# Write the necessary code to convert a degree in Fahrenheit
# to Celsius and print it to the console. Use variable names!

def degree():
    deg = int(input('enter degrees celsius : '))
    calc = (deg * 1.8 +32)
    print(f"{deg} degrees celsius equals {calc} degrees fahrenheit")

degree()