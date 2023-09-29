s = "0123"
s1 = "123"
k = 0
for x1 in s1:
    for x2 in s:
        for x3 in s:
            if x1 >= x2 >= x3:
                k += 1
print(k)
