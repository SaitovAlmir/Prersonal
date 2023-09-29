s = "АВИКЛ"
k = 0
for x1 in s:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                for x5 in s:
                    for x6 in s:
                        st = x1 + x2 + x3 + x4 + x5 + x6
                        k += 1
                        if (
                            st.count("А") <= 2
                            and st.count("В") == 2
                            and st.count("И") <= 0
                        ):
                            print(k, st)
