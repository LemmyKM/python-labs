# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """Kilometer to statute miles. Enter kilometers as an argument and output is X statute miles."""
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
print(km_to_miles(50))