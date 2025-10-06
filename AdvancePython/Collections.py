"""
COLLECTIONS : CENTER, NAMED_TUPLE,ORDERED_DICT, DEFAULT_DICT, DEQUE
"""

from collections import Counter
a = "aaaaaaaaabbbaaaccc"
my_counter = Counter(a)
print(my_counter)

print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

print(my_counter.most_common(1))
print(my_counter.most_common(2))

print(my_counter.most_common(1)[0])
print(my_counter.most_common(1)[0][0])

print(my_counter.elements())

print(list(my_counter.elements()))