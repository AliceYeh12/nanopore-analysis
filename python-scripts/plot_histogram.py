import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

pos = []
user_file = input("Enter file name: ")
out_file = input("Enter output name: ")
with open(user_file) as file:
    for line in file:
        pos.append(float(line))
        '''
        if (float(line) <= 2.0):
            pos.append(float(line))
        '''

#plt.hist(start_pos, bins=int(1.0/0.01), color='blue', edgecolor='black')
ax = sns.distplot(pos, bins=int(1.0/0.01), hist_kws={'edgecolor':'black'},
    kde_kws={'linewidth':3}, color='blue')

'''
ax = sns.distplot(pos, bins=int(2.0/0.0001), hist_kws={'edgecolor':'black'},
    kde_kws={'linewidth':3}, color='blue')

plt.xlim(0, 2.0)

'''
plot = ax.get_figure()
#plt.title("Start Position")
#plt.title("End Position")
plt.title("Transcript Coverage")
#plt.xlabel("Relative Strand Position")
plt.xlabel("Fraction of Strand")
plt.ylabel("Density")

plot.savefig(out_file)
#plt.savefig(out_file)
