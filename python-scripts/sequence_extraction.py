#Extracts sequence around start position.
start_dict = {}

refstart_file = input("Enter start position file name: ")
with open(refstart_file) as file:
    for line in file:
        try:
            (ref, start) = line.split()
            start_dict[ref] = start
        except:
            next(file)

transcript = input("Enter transcript file name: ")
out_file = input("Enter output file name: ")
with open(transcript) as file:
    ref_loc = 0
    seq_loc = 1
    lines = file.readlines()
    while seq_loc < len(lines):
        ref = lines[ref_loc].strip()
        ref = ref[1:]
        seq = lines[seq_loc].strip()
        try:
            start_pos = int(start_dict[ref])
            extracted = seq[(start_pos - 10):(start_pos + 11)]
            print(ref + " " + extracted, file=open(out_file, "a"))
            ref_loc += 2
            seq_loc += 2
        except:
            ref_loc += 2
            seq_loc += 2
