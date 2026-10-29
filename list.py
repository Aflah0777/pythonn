# 16.1 muthal 100 vare ulla oro number-um square cheyth list-il store cheyyum
# a = [x**2 for x in range(1, 101)]

# print(a)


# 17.String-il ulla capital letters mathram list-il edukkum
# a = "Hello WORLD Python"

# b = [x for x in a if x.isupper()]

# print(b)


# 18.Inner list-il ulla numbers ellam oru single list-il aakkum
# a = [[1, 2], [3, 4]]

# b = [x for i in a for x in i]

# print(b)


# 19.Even numbers square cheyyum; odd numbers same aayi irikkum
# a = [1, 2, 3, 4, 5, 6]

# b = [x**2 if x % 2 == 0 else x for x in a]

# print(b)


# 20.3 kondu divide cheyyan pattunna numbers mathram eduthu cube cheyyum
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# b = [x**3 for x in a if x % 3 == 0]

# print(b)


# 21.A, E, I, O, U enna vowels-il thudangunna words mathram list-il varum
# a = "apple is an orange and banana"

# b = [x for x in a.split() if x[0].lower() in "aeiou"]

# print(b)


# 22.Oro word-um reverse cheythu puthiya list undakkum
# a = ["apple", "banana", "mango"]

# b = [x[::-1] for x in a]

# print(b)


# 23.List-il None ulla places-il 0 varum
# a = [1, None, 3, None, 5]

# b = [0 if x is None else x for x in a]

# print(b)


# 24.Mixed list-il ninnu integers mathram edukkum
# a = [10, "hello", 20, 3.5, "hi", 30]

# b = [x for x in a if isinstance(x, int)]

# print(b)


# 25.First listile oro number-um second listile ella numbers-um aayi pair cheyyum
# a = [1, 2]
# b = [3, 4]

# c = [(x, y) for x in a for y in b]

# print(c)


# 26.Matrix-il left top muthal right bottom vare ulla diagonal numbers [1, 5, 9] aanu
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# b = [a[i][i] for i in range(len(a))]

# print(b)


# 27.1 muthal 5 vare ulla digits use cheythu ella two-digit pairs-um create cheyyum
# a = [1, 2, 3, 4, 5]

# b = [(x, y) for x in a for y in a]

# print(b)


# 28.Oro ID-yum athinte name-um combine cheythu dictionary undakkum
# id = [1, 2, 3]
# name = ["Aju", "Aflah", "Raju"]

# a = [{"id": i, "name": n} for i, n in zip(id, name)]

# print(a)


# 29.Temperature 30-inu mukalil aanenkil Hot, allenkil Cold
# a = [15, 25, 35, 10, 40]

# b = ["Hot" if x > 30 else "Cold" for x in a]

# print(b)


# 30.Integers mathram select cheythu string aakki maattum
# a = [10, 20.5, 30, 40.5, 50]

# b = [str(x) for x in a if isinstance(x, int)]

# print(b)
