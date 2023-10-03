# def f(a, b):
#     if a < b:
#         return 0
#     elif a == b:
#         return 1
#     else:
#         return f(a - 1, b) + f(a // 3, b)


# print(f(33, 9) * f(9, 1))


# def f(a, b):
#     if a > b:
#         return 0
#     elif a == b:
#         return 1
#     else:
#         return f(a + 2, b) + f(a * 2, b) + f(a * 3, b)


# print(f(1, 6) * f(6, 24))


# def f(a, b):
#     if a > b or a == 23:
#         return 0
#     elif a == b:
#         return 1
#     else:
#         return f(a + 1, b) + f(a * 2, b)


# print(f(3, 12) * f(12, 27))


def f(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(a + 3, b) + f(a * 2, b)


print(f(3, 8) * f(8, 11) * f(11, 14))
