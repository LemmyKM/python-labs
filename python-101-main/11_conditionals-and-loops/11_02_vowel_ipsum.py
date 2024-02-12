# Print the total number of vowels that are used in the lorem ipsum text.

lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum."""

low = lorem_ipsum.lower()

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for n in low:
    if n == 'a':
        count_a += 1
    elif n == 'e':
        count_e += 1
    elif n == 'i':
        count_i += 1
    elif n == 'o':
        count_o += 1
    else:
        if n == 'u':
            count_u += 1
print(count_a + count_e + count_i + count_o + count_u)