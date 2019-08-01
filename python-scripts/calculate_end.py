len_dict = {}

# Store reference names and the respective transcript length.
length_file = input("Enter sorted sequence length file name: ")
with open(length_file) as file:
    for line in file:
        try:
            (key, value) = line.split()
            len_dict[key] = value
        except:
            next(file)

# Uses start position and sequence to calculate end position with respect
# to transcript length.
end_pos_file = input("Enter data file name: ")
out_file = input("Enter output file name: ")
with open(end_pos_file) as file:
    for line in file:
        try:
            (ref, start, seq) = line.split()
            end = float(start) + len(seq)
            print(end/float(len_dict[ref]), file=open(out_file, "a"))
            '''
        try:
            (num, ref, start, seq) = line.split()
            end = float(start) + len(seq)
            print(num + " " + str(end/float(len_dict[ref])), file=open(out_file, "a"))
            '''
        except:
            next(file)
