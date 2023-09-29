s = "0123456789"
s1 = "12346789"
k = 0
for x1 in s1:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                if x1 == x2 or x2 == x3 or x3 == x4:
                    k += 1
print(k)
