# Combines two files by reference number.

start_file = input("Enter start file name: ")
x_file = input("Enter x file name: ")
out_file = input("Enter output file name: ")

start_dict = {}
with open(start_file) as file:
    for line in file:
        try:
            (ref, start) = line.split()
            start_dict[ref] = start
        except:
            next(file)

with open(x_file) as file:
    for line in file:
        try:
            (ref, per, seq) = line.split()
            start = start_dict[ref]
            print(start + " " + per, file=open(out_file, "a"))
        except:
            next(file)
