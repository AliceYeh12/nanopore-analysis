# Extracts minimum free energy (as a positive number) from RNAfold document.

in_file = input("Enter input file: ")
out_file = input("Enter output file: ")

mfe = []

with open(in_file) as file:
    count = 1
    for line in file:
        if (count % 3 == 0 and not (count % 6 == 0)):
            print("2 " + line[25:29], file=open(out_file, "a"))
        count += 1
