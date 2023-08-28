def grocery():
    d = {}
    while True:
        try:
            item = input().upper()
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1
        except KeyboardInterrupt:
            print()
            break
    sorted_dict = {key: value for key, value in sorted(d.items())}
    for i in sorted_dict:
        print(sorted_dict[i], i)

grocery()