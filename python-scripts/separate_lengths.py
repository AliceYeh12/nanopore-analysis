# Divides transcripts into bins by length.

def main():
    len_dict = {}
    num_dict = {}

    sorted_file = input("Enter sorted sequence length file name: ")
    with open(sorted_file) as file:
        for line in file:
            try:
                (key, value) = line.split()
                len_dict[key] = value
                value = int(value)
                interval = findInterval(value)
                num_dict[key] = interval
            except:
                next(file)

    cln_file = input("Enter cleaned file name: ")
    out_file = input("Enter output file name: ")
    with open(cln_file) as file:
        for line in file:
            try:
                (ref, start, seq) = line.split()
                num = num_dict[ref]
                #print(str(num) + " " + str(len(seq)/float(len_dict[ref])), file=open(out_file, "a"))
                print(str(num) + " " + str((float(start)/float(len_dict[ref]))), file=open(out_file, "a"))
            except:
                next(file)

def findInterval(value):
    if value < 1000:
        return 1
    elif value >= 1000 and value < 2500:
        return 2
    elif value >= 2500 and value < 5000:
        return 3
    elif value >= 5000 and value < 10000:
        return 4
    else:
        return 5

if __name__ == '__main__':
    main()
