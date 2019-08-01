# Plots a boxplot for GC content, stratified by start position.

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
            (start, content) = line.split()
            start = categorize(float(start))
            content = float(content[:len(content)-1])
            data.append(({"Relative Strand Position":start, "GC Content (%)":content}))

    df = pd.DataFrame(data)
    sns.boxplot(x="Relative Strand Position", y="GC Content (%)", data=df,
        order=["0.0 - 0.2", "0.2 - 0.4", "0.4 - 0.6", "0.6 - 0.8", "0.8 - 1.0"])

    plt.title("GC Content by Start Position")
    plt.savefig(out_file)

def categorize(start):
    if start <= 0.2:
        return "0.0 - 0.2"
    elif start <= 0.4:
        return "0.2 - 0.4"
    elif start <= 0.6:
        return "0.4 - 0.6"
    elif start <= 0.8:
        return "0.6 - 0.8"
    else:
        return "0.8 - 1.0"

if __name__ == '__main__':
    main()
