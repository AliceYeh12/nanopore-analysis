# Calculates the amount of transcript coverage for each read.

len_dict = {}

length_file = input("Enter sorted sequence length file name: ")
with open(length_file) as file:
    for line in file:
        try:
            (key, value) = line.split()
            len_dict[key] = value
        except:
            next(file)

cleaned_file = input("Enter cleaned file name: ")
out_file = input("Enter output file name: ")
with open(cleaned_file) as file:
    for line in file:
        try:
            (ref, start, seq) = line.split()
            print(ref+ " " + str(len(seq)/float(len_dict[ref])), file=open(out_file, "a"))
        except:
            next(file)
