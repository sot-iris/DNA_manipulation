def text(x):
    list1 = []
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
    for i in x:
        if i not in numbers:
            list1.append(i)

    print "".join(map(str, list1)),

text("""Replace this text with your DNA seq""")
