# a = 10
# b = -1
# r = true
# for i in range(a * 2 - 2):
#     if a > 1 and r:
#         a -= 1
#         b += 2
#         print(a * "-", b * "*", a * "-")
#     elif a == 1 and r:
#         r = false
#     elif a > 0 and not r:
#         a += 1
#         b -= 2
#         print(a * "-", b * "*", a * "-")
#     elif a == 20 and not r:
#         r = true


# Diamond shape
# def Diamond(rows):
#     n = 0
#     for i in range(1, rows + 1):
#         # loop to print spaces
#         for j in range(1, (rows - i) + 1):
#             print(end=" ")
#
#             # loop to print star
#         while n != (2 * i - 1):
#             print("*", end="")
#             n = n + 1
#         n = 0
#
#         # line break
#         print()
#
#     k = 1
#     n = 1
#     for i in range(1, rows):
#         # loop to print spaces
#         for j in range(1, k + 1):
#             print(end=" ")
#         k = k + 1
#
#         # loop to print star
#         while n <= (2 * (rows - i) - 1):
#             print("*", end="")
#             n = n + 1
#         n = 1
#         print()
#
#
# # number of rows input
# rows = 5
# Diamond(rows)
