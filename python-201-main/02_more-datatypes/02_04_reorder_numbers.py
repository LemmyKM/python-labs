# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1

lijst = [1,2,3,4,5,6,7,8,9,10]
even_lijst = []
oneven_lijst = []
for x, y in enumerate(lijst, start=1):
    if x % 2 == 0:
        even_lijst.append(y)
print(even_lijst)

for x, y in enumerate(lijst, start=1):
    if x % 2 != 0:
        oneven_lijst.append(y)

omgekeerd = oneven_lijst[::-1]
print(even_lijst + omgekeerd)



