from collections import deque

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)

print(d)

d.popleft()
print(d)

d.extend([4,5,6])
d.extendleft([8,9,0])
print(d)
d.rotate(1)
print(d)
d.rotate(-3)
print(d)