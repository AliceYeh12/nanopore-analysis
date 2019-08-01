# Tracks nucleotide frequency from sequence inputs.

GTCA = [0, 0, 0, 0]
start_pos_file = input("Enter data file name: ")
with open(start_pos_file) as file:
    for line in file:
        try:
            (num, ref, start, seq) = line.split()
            nuc = list(seq)
            if nuc[len(seq)-1] == "G":
                GTCA[0] += 1
            elif nuc[len(seq)-1] == "T":
                GTCA[1] += 1
            elif nuc[len(seq)-1] == "C":
                GTCA[2] += 1
            else:
                GTCA[3] += 1
        except:
            next(file)

print(GTCA)
