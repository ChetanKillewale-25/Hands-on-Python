mult = lambda x,y: x*y
print(mult(3,0))

points_2d = [(1,90),(15,6),(9,6)]
points_2d_sorted = sorted(points_2d)
print(points_2d_sorted)

sort1 = sorted(points_2d, key = lambda x: x[1])
"""
def sort-[0}:
    return x[1]
"""
print(sort1)

sort2 = sorted(points_2d, key = lambda x: x[0]+x[1])
print(sort2)