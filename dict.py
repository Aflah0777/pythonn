# 1.Oro number-um key aayum, athinte cube value aayum dictionary-il store cheyyum
# a = {x: x**3 for x in range(1, 21)}

# print(a)


# 2.String-il ulla oro vowel-um ethra pravashyam varunnu ennu count cheyth dictionary-il store cheyyum
# a = "hello world"

# b = {x: a.count(x) for x in "aeiou" if x in a}

# print(b)


# 3.Oro word-um key aayum, athinte reverse value aayum dictionary-il store cheyyum
# a = ["apple", "banana", "mango"]

# b = {x: x[::-1] for x in a}

# print(b)


# 4.None value ulla tuples skip cheyyum. Baaki tuples dictionary aakki print cheyyum
# a = [("a", 10), ("b", None), ("c", 30), ("d", None)]

# b = {k: v for k, v in a if v is not None}

# print(b)


# 5.Oro item-inte price-il ninnu 10% discount kurachu new dictionary-il store cheyyunnu.
# items = {"apple": 100, "banana": 50, "mango": 200}

# discount = 10

# dd = {k: v - (v * discount / 100) for k, v in items.items()}

# print(dd)


# 6.Key-inte first letter vowel (a, e, i, o, u) aanenkil dictionary-il keep cheyyum
# d = {"apple": 10, "banana": 20, "orange": 30, "grapes": 40, "elephant": 50}

# dd = {k: v for k, v in d.items() if k[0].lower() in "aeiou"}

# print(dd)


# 7.List-il oro item-inte position (index) um value-um dictionary-il store cheyyunnu. Index 0-il ninnanu start cheyyunnathu
# a = ["apple", "banana", "mango", "orange"]

# d = {i: v for i, v in enumerate(a)}

# print(d)


# 8.Number zero-nekkal valuthaanenkil positive, cheruthaanenkil negative, zero aanenkil zero enn dictionary-il store cheyyum
# a = [-5, -2, 0, 3, 8]

# d = {x: "positive" if x > 0 else "negative" if x < 0 else "zero" for x in a}

# print(d)


# 9.Sentence-il oro word ethra thavana varunnu ennu count cheythu dictionary-il store cheyyunnu.
# a = "apple banana apple mango banana apple"

# words = a.split()

# d = {x: words.count(x) for x in words}

# print(d)


# 10.Original dictionary-il oru thavana mathram varunna values-ne keep cheythu key-um value-um reverse cheyyunnu.
# d = {"a": 10, "b": 20, "c": 10, "d": 30}

# dd = {v: k for k, v in d.items() if list(d.values()).count(v) == 1}

# print(dd)


# 11.Prime number aanenkil True, prime allenkil False. Example: 2 → True, 4 → False, 7 → True.
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# d = {x: x > 1 and all(x % i != 0 for i in range(2, x)) for x in a}

# print(d)


# 12.List-il oro item ethra thavana varunnu ennu count cheythu dictionary-il store cheyyunnu.
# a = ["apple", "banana", "apple", "mango", "banana", "apple"]

# d = {x: a.count(x) for x in a}

# print(d)


# 13.Number 2 kondu divide cheyyumbol remainder 0 aanenkil even, allenkil odd aayi dictionary-il store cheyyum
# d = {x: "even" if x % 2 == 0 else "odd" for x in range(1, 31)}

# print(d)


# 14.Randu list-ukaludeyum length same aanenkil dictionary create cheyyum. Length different aanenkil empty dictionary print cheyyum
# a = ["name", "age", "place"]
# b = ["Basu", 21, "Kerala"]

# d = {a[i]: b[i] for i in range(len(a))} if len(a) == len(b) else {}

# print(d)


# 15.Mark 40-o athil kooduthalo aanenkil Pass, 40-il thazhe aanenkil Fail aayi dictionary-il store cheyyum
marks = {"Aju": 80, "Basu": 35, "Riya": 25, "Aman": 60}

d = {k: "Pass" if v >= 40 else "Fail" for k, v in marks.items()}

print(d)