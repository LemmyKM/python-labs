# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."
for x, y in enumerate(s):
    print(x, y)


een = s[5:9] + s[2]
print(een)

twee = s[-9] + s[73:76]
print(twee)

drie = s[57:63]
print(drie)

vier = s[7:12]
print(vier)