# Plots stacked bar graph of dinucleotide frequencies, stratified by start position.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

def main():
    file_name = input("Enter file name: ")
    out_file = input("Enter output file name: ")
    data = []
    dinucleotides = ['AA', 'AC', 'AG', 'AT', 'CA', 'CC', 'CG', 'CT', 'GA', 'GC', 'GG',
        'GT', 'TA', 'TC', 'TG', 'TT']

    percentages = []
    count = 1
    with open(file_name) as file:
        for line in file:
            dicount = 0
            line = line.rstrip()
            percentages = line.split(" ")
            category = findCategory(count)
            for x in percentages:
                data.append(({"Relative Strand Position":category, "Dinucleotide Frequency (%)":float(x),
                    "Dinucleotides":dinucleotides[dicount]}))
                dicount += 1
            count += 1

    df = pd.DataFrame(data)
    pivot_df = df.pivot(index="Relative Strand Position", columns="Dinucleotides",
        values="Dinucleotide Frequency (%)")

    ax = pivot_df.plot.bar(stacked=True, colormap='tab20')

    chartBox = ax.get_position()
    ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(reversed(handles), reversed(labels), loc='upper center', bbox_to_anchor=(1.2, 0.98), shadow=True, ncol=1)

    ax.set_xticklabels(ax.get_xticklabels(), rotation=360)

    plt.xlabel("Fraction of Strand Covered")
    plt.ylabel("Dinucleotide Frequency (%)")
    plt.title("Dinucleotide Frequency by Transcript Coverage")
    plt.savefig(out_file)

def findCategory(count):
    if count == 1:
        return "0.0-0.2"
    elif count == 2:
        return "0.2-0.4"
    elif count == 3:
        return "0.4-0.6"
    elif count == 4:
        return "0.6-0.8"
    else:
        return "0.8-1.0"

if __name__ == '__main__':
    main()
