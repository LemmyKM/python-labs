lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

while True: # Keep asking until the user enters e or d.
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    if response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter "e" or "d"')


while True:
    maxKey = len(lowercase_letters) - 1
    print(f"Please enter the key (0 to {maxKey}) to use.")
    response = input('> ').lower()
    if not response.isdecimal:
        continue

    if 0 <= int(response) < len(lowercase_letters):
        key = int(response)
        break

print(f"Enter the message to {mode}")
message = input('> ')