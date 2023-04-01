ip="aaabbccccaabbbbbddddd"
t = []
t1 = ""
count = 0
for i in ip:  
    if t1 != i:
        count = 1
        t1 = i
    else: count += 1
    t.append((t1, count))    
print(t)

# a-3, b-2, c-4, a-2, b-5, d-5