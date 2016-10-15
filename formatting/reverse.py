seq1 = raw_input("Enter your sequence: ")
seq = seq1.upper()

list = []

def comp(x):
    for n in x:
        if n == "A":
            list.append("T")
        elif n == "T":
            list.append("A")
        elif n == "C":
            list.append("G")
        elif n == "G":
            list.append("C")
        else:
            list.append("X")

comp(seq)
print "Complimentary base pairs: " + ''.join(list)
print "Reverse complimentary: " + ''.join(list[::-1])
