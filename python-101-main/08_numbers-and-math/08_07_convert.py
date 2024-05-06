# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions? decimal is lost during
# float divided by integer.

a = 3
a1 = float(a)
print(a1)

b = 6.0
b1 = int(b)
print(b1)

c = 6.0
d = 3
c_div_d = c / d
print(c_div_d)

e = 3
f = 7
multip = e * f
print(multip)