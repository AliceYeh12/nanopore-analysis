#Plots a boxplot for GC content, stratified by start position.

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
            data.append(({"Transcript Length":start, "GC Content (%)":content}))

    df = pd.DataFrame(data)
    sns.boxplot(x="Transcript Length", y="GC Content (%)", data=df,
        order=["<1,000", "1,000-2,500", "2,500-5,000", "5,000-10,000", "10,000+"])

    plt.title("GC Content by Transcript Length")
    plt.savefig(out_file)

def categorize(value):
    if value < 1000:
        return "<1,000"
    elif value >= 1000 and value < 2500:
        return "1,000-2,500"
    elif value >= 2500 and value < 5000:
        return "2,500-5,000"
    elif value >= 5000 and value < 10000:
        return "5,000-10,000"
    else:
        return "10,000+"

if __name__ == '__main__':
    main()
