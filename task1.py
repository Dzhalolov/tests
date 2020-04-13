def check():
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    a = random.choice(lst)
    inter = lst.copy()
    inter.remove(a)
    b = random.choice(inter)
    inter.remove(b)
    choice_first = random.choice(inter)
    choice_first_increment = lst[0]

    if choice_first != lst[-1]:
        choice_first_increment = choice_first + 1
    lst.remove(choice_first)
    result = []

    if a == choice_first_increment or b == choice_first_increment:
        result.append(1)
    choice_second = random.choice(lst)

    if a == choice_second or b == choice_second:
        result.append(2)


    return result


count_1 = 0; count_2 = 0
for _ in range(1000000):
    if 1 in check():
        count_1 += 1
    if 2 in check():
        count_2 += 1

# count_1 = 285834
# count_2 = 285559
# погрешность минимальная, значит они равны