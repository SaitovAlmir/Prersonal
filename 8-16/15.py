s = "123456"
k = 0
for x1 in s:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                for x5 in s:
                    st = x1 + x2 + x3 + x4 + x5
                    if st.count("1") == 1:
                        k += 1
print(k)
