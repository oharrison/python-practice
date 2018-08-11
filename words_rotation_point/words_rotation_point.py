def rotation_point(words):
    start_point = 0
    end_point = len(words) - 1
    mid_point = end_point // 2

    while start_point <= end_point:
        if words[mid_point] < words[mid_point - 1]:
            return mid_point
        elif words[mid_point] < words[start_point]:
            end_point = mid_point - 1
            mid_point = (end_point + start_point) // 2
        elif words[mid_point] > words[start_point]:
            start_point = mid_point + 1
            mid_point = (end_point + start_point) // 2
        else:
           return 0

    return None

if __name__ == '__main__':
    words_0 = [
        'ptolemaic',
        'retrograde',
        'supplant',
        'undulate',
        'xenoepist',
        'asymptote',
        'babka',
        'banofee',
        'engender',
        'karpatka',
        'othellolagkage'
    ]
    assert rotation_point(words_0) == 5

    words_1 = ['apples', 'berries', 'caramel', 'dip', 'enchiladas']
    assert rotation_point(words_1) == 0

    words_2 = ['berries', 'caramel', 'dip', 'xylophone', 'apples']
    assert rotation_point(words_2) == 4

    assert rotation_point([]) == None
