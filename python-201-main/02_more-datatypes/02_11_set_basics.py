# With the given sets `s` and `t`, demonstrate how you can:
# - Create an intersection of both sets
# - Create a union of both sets

s = {1, 2, 3, 4}
t = {3, 4, 5, 6}

intersect = s.intersection(t)
print(intersect)
#or
intersect2 = s & t
print(intersect2)


together = s | t
print(together)
#or
together2 = s.union(t) # !!! met '.union()' kan je niet enkel 'sets' samenvoegen. bv ook 'lists' en 'sets'
print(together2)