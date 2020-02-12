len_dict = {}

# Store reference names and the respective transcript length.
length_file = "sslb.txt"
with open(length_file) as file:
    for line in file:
        try:
            (key, value) = line.split()
            len_dict[key] = value
        except:
            next(file)

# Calculates start position with respect to transcript length.
start_pos_file = "startpos.txt"
out_file = "relstart.txt"
with open(start_pos_file) as file:
    for line in file:
        try:
            (ref, start, seq) = line.split()
            start = float(start)
            print(ref + " " + str(start/float(len_dict[ref])), file=open(out_file, "a"))
            '''
        try:
            (num, ref, start, seq) = line.split()
            start = float(start)
            print(num + " " + str(start/float(len_dict[ref])), file=open(out_file, "a"))
        '''
        except:
            next(file)
