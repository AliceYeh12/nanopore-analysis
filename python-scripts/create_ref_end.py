# Creates guide with reference and end position.

in_file = input("Enter file name: ")
out_file = input("Enter output file name: ")

with open(in_file) as file:
    for line in file:
        try:
            (ref, start, seq) = line.split()
            end = int(start) + len(seq)
            print(ref + " " + str(end), file=open(out_file, "a"))
        except:
            next(file)
