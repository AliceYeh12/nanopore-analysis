# Plots violin plots for each length bin.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    sns.set()
    data = []

    file_name = input("Enter file name: ")
    out_file = input("Enter output file name: ")
    with open(file_name) as file:
        for line in file:
            (len, cov) = line.split()
            cov = float(cov)
            len = convertNum(len)
            data.append(({"Relative Strand Position":cov, "Transcript Length":len}))

    df = pd.DataFrame(data)
    ax = sns.violinplot(x="Transcript Length", y="Relative Strand Position", data=df,
        order=["<1,000", "1,000-2,500", "2,500-5,000", "5,000-10,000", "10,000+"])

    plt.title("Start Position by Length")
    plt.savefig(out_file)

def convertNum(num):
    if num == "1":
        return "<1,000"
    elif num == "2":
        return "1,000-2,500"
    elif num == "3":
        return "2,500-5,000"
    elif num == "4":
        return "5,000-10,000"
    else:
        return "10,000+"

if __name__ == '__main__':
    main()
