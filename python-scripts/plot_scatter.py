import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

def main():
    data = []
    comb_file = input("Enter combined file name: ")
    out_file = input("Enter output name: ")
    with open(comb_file) as file:
        for line in file:
            (num, start, end) = line.split()
            num = convertNum(num)
            data.append(({'Length':num, 'Start Position':float(start), 'End Position':float(end)}))

    df = pd.DataFrame(data)

    ax = sns.lineplot(x='Start Position', y='End Position', data=df, hue='Length')
    #ax.legend(ncol = 2, loc = 'upper left')

    #plt.xlabel("Start Position")
    #plt.ylabel("End Position")
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
