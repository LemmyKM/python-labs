# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

name = input('Please enter your name : ')

split_name = name.split()
first_word = split_name[0]

print(f"Good morning {first_word}. Welcome to this intergalaxy flight to Zarxon. Please fasten your seat belt.")