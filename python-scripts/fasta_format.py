# Creates FASTA file format from text with reference and sequence.

input_file = "refseq.txt"
out_file = "refseq.fa"

seq_dict = []
with open(input_file) as file:
    for line in file:
        try:
            (ref, start, seq) = line.split()
            if float(start) > 0.8:
                print(">" + ref + "\n" + seq, file=open(out_file, "a"))
        except:
            next(file)
