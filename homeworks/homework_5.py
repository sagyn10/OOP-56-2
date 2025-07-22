from homeworks.distance import Distance

d1 = Distance(100, "см")
d2 = Distance(50, "см")
d3 = Distance(70, "см")
d4 = Distance(30, "см")

print(d1)
print(d1 + d2)
print(d3 - d4)
print(d1 == Distance(100, "см"))
print(d1 > d2)
print(d2 < d3)











