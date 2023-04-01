x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
# t = []
# for i in points:
#     t.append(abs(i[0]-x)+abs(i[1]-y))
# close = min(t)
# print(t.count(close))

t = [abs(i[0]-x)+abs(i[1]-y) for i in points]
close = t.count(min(t))
print(close)

