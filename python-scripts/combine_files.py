# Combines two files.

start_file = "start.txt"
end_file = "end.txt"
out_file = "comb.txt"

with open(start_file) as start, open(end_file) as end:
    for s, e in zip(start, end):
        print(s.strip() + " " + e.strip(), file=open(out_file, "a"))
