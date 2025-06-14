def count():
    d = {}
    with open("Names.txt", 'r') as f:
        names = f.readlines()
        for name in names:
            name = name.strip()
            if name in d:
                d[name] += 1
            else:
                d[name] = 1
    print(d)
