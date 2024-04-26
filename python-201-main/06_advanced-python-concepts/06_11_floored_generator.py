# Adapt your Generator expression from the previous exercise:
# Add a floor division by 1111 on it.
# What numbers do you get?

nums = range(1, 1000000)



gen = (x for x in nums if x // 1111)
for x in gen:
    print(x)

# these are all the numbers from 1 to 1000000