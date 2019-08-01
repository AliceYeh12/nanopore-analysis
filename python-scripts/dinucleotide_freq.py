#Calculates the dinucleotide frequency for each bin (separate by start position).

one = {}
two = {}
three = {}
four = {}
five = {}

def main():
    num_dict = {}
    refs = []
    seqs = []

    ref_file = input("Enter reference file name: ")
    dinuc_file = input("Enter dinucleotide frequency file name: ")
    out_file = input("Enter output file name: ")

    with open(ref_file) as file:
        for line in file:
            try:
                (ref, num) = line.split()
                num_dict[ref] = num
            except:
                next(file)

    with open(dinuc_file) as file:
        for line in file:
            try:
                (ref, seq) = line.split()
                refs.append(ref)
                seqs.append(seq)
            except:
                next(file)

    for seq in seqs:
        num = num_dict[refs[seqs.index(seq)]]
        categorize(num, seq)

    output(one, out_file)
    output(two, out_file)
    output(three, out_file)
    output(four, out_file)
    output(five, out_file)

def categorize(num, seq):
    num = float(num)
    if num <= 0.2:
        addNuc(one, seq)
    elif num <= 0.4:
        addNuc(two, seq)
    elif num <= 0.6:
        addNuc(three, seq)
    elif num <= 0.8:
        addNuc(four, seq)
    else:
        addNuc(five, seq)

def addNuc(dinuc_dict, seq):
    pos1 = 0
    pos2 = 1
    dinucleotide = ""
    while (pos2 < len(seq)):
        dinucleotide = seq[pos1] + seq[pos2]
        if dinucleotide in dinuc_dict:
            dinuc_dict[dinucleotide] += 1
        else:
            dinuc_dict[dinucleotide] = 1
        pos1 += 1
        pos2 += 1

def output(dict, out_file):
    sum = 0
    for key in sorted(dict.keys()):
        sum += int(dict[key])

    for key in sorted(dict.keys()):
        print("%s" % ((float(int(dict[key])/sum))*100), end=" ", file=open(out_file, "a"))

    print(file=open(out_file, "a"))

if __name__ == '__main__':
    main()
