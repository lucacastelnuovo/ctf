input = [
    (35, 35, 35),
    (255, 255, 255),
    (0, 0, 0),
    (47, 47, 47),
    (0, 0, 0),
    (149, 149, 149),
    (47, 47, 47),
    (90, 90, 90),
    (0, 0, 0),
    (10, 10, 10),
    (31, 31, 31),
    (255, 255, 255),
    (124, 124, 124),
    (75, 75, 75),
    (0, 0, 0),
    (118, 118, 118),
    (115, 115, 115),
    (208, 208, 208),
    (0, 0, 0),
    (54, 54, 54),
    (28, 28, 28),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (172, 172, 172),
    (45, 45, 45),
    (86, 86, 86),
    (255, 255, 255),
    (132, 132, 132),
    (0, 0, 0),
    (91, 91, 91),
    (0, 0, 0),
    (255, 255, 255),
    (177, 177, 177),
    (60, 60, 60),
]


def removeDuplicates(lst):
    return [t for t in (set(tuple(i) for i in lst))]


print(removeDuplicates(input))
