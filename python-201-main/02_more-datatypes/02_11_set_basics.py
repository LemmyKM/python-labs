# With the given sets `s` and `t`, demonstrate how you can:
# - Create an intersection of both sets
# - Create a union of both sets

s = {1, 2, 3, 4}
t = {3, 4, 5, 6}
u = [7, 8, 9, 10]

intersect = s.intersection(t)
print(f"\nThe intersection (&) of 's' and 't' is {intersect}; code = s & t.")
#or
# intersect2 = s & t
# print(intersect2)


union = s | t
print(f"\nThe union (|) of 's' and 't' is {union}; code = s | t.")
#or
# together2 = s.union(t) # !!! met '.union()' kan je niet enkel 'sets' samenvoegen. bv ook 'lists' en 'sets'
# print(together2)


t_en_u = t.union(u)
print(f"\nThe union (.union()) of 't' and 'u' is {t_en_u}; code = t.union(u) which allows to combine 'lists' and 'sets'.")