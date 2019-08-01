# Removes duplicates from a file.

prev_ref = " "

file_name = input("Enter file name: ")
out_file = input("Enter output file name: ")
with open(file_name) as file:
    for line in file:
        try:
            (ref, length) = line.split()
            if not (ref == prev_ref):
                print(ref + " " + length, file=open(out_file, "a"))
            prev_ref = ref
        except:
            next(file)
