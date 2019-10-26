def rotate_left(list_numbers, k):
    def rotate(a, l, h):
        while l < h:
            a[l], a[h] = a[h], a[l]
            l += 1
            h -= 1

    k %= len(list_numbers)
    s = len(list_numbers)
    rotate(list_numbers, 0, s - 1)
    rotate(list_numbers, 0, s - 1 - k)
    rotate(list_numbers, s - k, s - 1)

    return list_numbers


ARRAY = 'array'
POSITIONS = 'positions'

tests = [
    {
        ARRAY: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        POSITIONS: 4
    },
    {
        ARRAY: [1],
        POSITIONS: 7
    },
    {
        ARRAY: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        POSITIONS: 14
    },
    {
        ARRAY: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        POSITIONS: 2
    },
    {
        ARRAY: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        POSITIONS: 10
    }
]

for t in tests:
    print(t[ARRAY], t[POSITIONS])
    print(rotate_left(t[ARRAY], t[POSITIONS]))
