# Creates guide with reference and end position.

in_file = "input.txt"
out_file = "combguide.txt"

with open(in_file) as file:
    for line in file:
        try:
            (ref, start, seq) = line.split()
            end = int(start) + len(seq)
            print(ref + " " + str(end), file=open(out_file, "a"))
        except:
            next(file)
