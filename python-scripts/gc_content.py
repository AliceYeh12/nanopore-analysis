#Calculates the GC content of each sequence.

refs = []
seqs = []
content = []
in_file = input("Enter file name: ")
with open(in_file) as file:
    for line in file:
        try:
            (ref, seq) = line.split()
            refs.append(ref)
            seqs.append(seq)
        except:
            next(file)

for seq in seqs:
    count = 0
    for nuc in seq:
        if (nuc == "G" or nuc == "C"):
            count += 1
    content.append(float(count/len(seq)) * 100)

out_file = input("Enter output file name: ")
for i in range(0, len(refs)):
    print(refs[i] + " " + str(content[i]) + "% " + seqs[i], file=open(out_file, "a"))
