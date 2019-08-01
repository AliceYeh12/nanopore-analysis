# Length limiting version of CleanAlignments.py.

from collections import Counter

def main():
    ref_name = []  # strings
    start_pos = []  # ints
    seq = []  # strings of sequences
    end_pos = []
    ref_count = {}

    long_seq_num = []  # position of sequences that pass the 90% test
                       # in the lists above

    len_dict = {}  # reference for length of each transcript

    ref_name_new = []  # contains reference names of sequences that
                       # passed 90% test
    start_pos_new = []
    seq_new = []

    end_pos_new = []
    ref_new_count = {}

    ref_file = input("Enter sorted sequence length file name: ")
    with open(ref_file) as file:
        for line in file:
            try:
                (key, value) = line.split()
                len_dict[key] = value
            except:
                next(file)

    # Reads in data regarding reference name and start position and the
    # sequence.
    file_name = input("Enter input (sorted end position) file name: ")
    out_file = input("Enter output file name: ")
    with open(file_name) as file:
        for line in file:
            (ref, start, aln) = line.split()
            ref_name.append(ref)
            start_pos.append(start)
            seq.append(aln)
            end_pos.append(int(start) + len(aln))

    ref_count = Counter(ref_name)

    # Selects for only the reads whose lengths are at least 90% of the
    # longest alignment and end within the transcript length.
    pos = 0
    while (pos < len(ref_name)):
        num_tr = ref_count[ref_name[pos]]
        length = getLongest(num_tr, seq, pos)
        for num in range(0, num_tr):
            try:
                if (float(len(seq[pos])/length) >= 0.90 and
                    float(int(end_pos[pos])/int(len_dict[ref_name[pos]])) <= 1.05):
                    long_seq_num.append(pos)
                pos += 1
            except:
                pos += num_tr

    for num in long_seq_num:
        ref_name_new.append(ref_name[num])
        start_pos_new.append(start_pos[num])
        seq_new.append(seq[num])
        end_pos_new.append(int(start_pos[num]) + len(seq[num]))

    ref_new_count = Counter(ref_name_new)

    # Selects for the read that ends (or more technically, starts,) closest
    # to the end position.
    pos = 0
    while (pos < len(ref_name_new)):
        num_tr = ref_new_count[ref_name_new[pos]]
        try:
            actual_len = len_dict[ref_name_new[pos]]
            best_pos = findBest(num_tr, actual_len, end_pos, pos)
            print(ref_name_new[best_pos] + " " + start_pos_new[best_pos] + " " +
                seq_new[best_pos], file=open(out_file, "a"))
            pos += num_tr
        except:
            pos += num_tr

# Gets the length of the longest alignment.
def getLongest(num_tr, seq, pos):
    longest = 0.0
    for num in range(0, num_tr):
        longest = max(len(seq[pos]), longest)
        pos += 1
    return longest

# Finds the read that ends closest to the end position.
def findBest(num_tr, actual_len, end_pos, pos):
    best = 99999999
    best_pos = 0
    for num in range(0, num_tr):
        diff = int(end_pos[pos]) - int(actual_len)
        if (abs(diff) < best and diff <= 0.05):
            best = abs(diff)
            best_pos = pos
    return best_pos

if __name__ == '__main__':
    main()
