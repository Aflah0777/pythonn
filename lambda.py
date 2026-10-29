# 1.abs() always returns a non-negative value
# diff = lambda a, b: abs(a - b)

# print(diff(10, 5))


# 2.Oro integer-ineyum string aakki maattum, Basu. For example, 1 becomes '1'
# a = [1, 2, 3, 4, 5]

# b = list(map(lambda x: str(x), a))

# print(b)


# 3.Base 10, height 5. Formula use cheyth area calculate cheyyum
# area = lambda b, h: 0.5 * b * h

# print(area(10, 5))


# 4.Number-ne 10 kondu divide cheyyumbol remainder 5 aanenkil, aa number output-il varum
# a = [15, 22, 35, 48, 55, 60]

# b = list(filter(lambda x: x % 10 == 5, a))

# print(b)


# 5.Oro tuple-ilum second value nokki ascending order-il sort cheyyum
# a = [(1, 30), (2, 10), (3, 20)]

# b = sorted(a, key=lambda x: x[1])

# print(b)


# 6.String-il a undenkil True, illenkil False print cheyyum
# check = lambda s: 'a' in s

# print(check("apple"))


7.
# mul = lambda a, b, c: a * b * c

# print(mul(2, 3, 4))


# 8.Word thirichu vayichalum same aanenkil athu palindrome aanu. Example: madam
# a = ["madam", "hello", "level", "world", "radar"]

# b = list(filter(lambda x: x == x[::-1], a))

# print(b)


# 9.List-il ulla oro number-inodum 10 add cheyyum
# a = [1, 2, 3, 4, 5]

# b = list(map(lambda x: x + 10, a))

# print(b)


# 10.Oro name-inte length nokki short name muthal long name vare sort cheyyum,
# a = [
#     {"name": "Aflah"},
#     {"name": "Ali"},
#     {"name": "Rahul"}
# ]

# b = sorted(a, key=lambda x: len(x["name"]))

# print(b)


# 11.Number 10 muthal 50 vare aanenkil True print cheyyum
# check = lambda x: 10 <= x <= 50

# print(check(25))


# 12.List-il ulla ella numbers-um multiply cheythu final answer 120 kittum
# from functools import reduce

# a = [1, 2, 3, 4, 5]

# b = reduce(lambda x, y: x * y, a)

# print(b)


# 13.Oro word-inte first letter capital aakkum
# a = ["apple", "banana", "mango"]

# b = list(map(lambda x: x.capitalize(), a))

# print(b)


# 14.Prime number 1-um thanne-yum mathram divide cheyyan pattunna number aanu. Example: 2, 3, 5, 7
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# b = list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, x)), a))

# print(b)


# 15.Oro price-inte munpilum ₹ symbol add cheyyum,
# a = [100, 200, 300, 400]

# b = list(map(lambda x: "₹" + str(x), a))

# print(b)