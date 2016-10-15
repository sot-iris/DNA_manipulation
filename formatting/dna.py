def text(x):
    list1 = []
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
    for i in x:
        if i not in numbers:
            list1.append(i)

    seq = "".join(map(str, list1))
    print seq.upper()

text("""Enter your GenBank-style sequence here to convert to Plain Text Format with no numbers or spaces""")
