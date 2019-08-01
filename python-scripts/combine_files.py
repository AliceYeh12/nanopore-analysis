# Combines two files.

start_file = input("Enter start file name: ")
end_file = input("Enter end file name: ")
out_file = input("Enter output file name: ")

with open(start_file) as start, open(end_file) as end:
    for s, e in zip(start, end):
        print(s.strip() + " " + e.strip(), file=open(out_file, "a"))
