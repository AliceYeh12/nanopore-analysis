# Plots a boxplot for minimum free energy, stratified by start position.

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
            (bin, mfe) = line.split()
            bin = categorize(int(bin))
            mfe = -1 * float(mfe[:len(mfe)-1])
            data.append(({"Relative Strand Position":bin, "Minimum Free Energy":mfe}))

    df = pd.DataFrame(data)
    sns.boxplot(x="Relative Strand Position", y="Minimum Free Energy", data=df,
        order=["0.0 - 0.2", "0.2 - 0.4", "0.4 - 0.6", "0.6 - 0.8", "0.8 - 1.0"])

    plt.title("Minimum Free Energy by Start Position")
    plt.savefig(out_file)

def categorize(bin):
    if bin == 1:
        return "0.0 - 0.2"
    elif bin == 2:
        return "0.2 - 0.4"
    elif bin == 3:
        return "0.4 - 0.6"
    elif bin == 4:
        return "0.6 - 0.8"
    else:
        return "0.8 - 1.0"

if __name__ == '__main__':
    main()
