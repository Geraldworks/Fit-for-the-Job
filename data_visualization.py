import matplotlib.pyplot as plt
import seaborn as sns

# Function to plot a bar graph of the frequency of a specific column
def plot_column_frequency(data, column_name, title='Frequency Bar Graph', xlabel='Categories', ylabel='Frequency'):
    plt.figure(figsize=(10, 6))
    sns.set(style="whitegrid")
    ax = sns.countplot(data=data, x=column_name, palette="viridis")
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='baseline', fontsize=12, color='black', xytext=(0, 5), textcoords='offset points')
    plt.title(title, fontsize=18)
    plt.xlabel(xlabel, fontsize=15)
    plt.ylabel(ylabel, fontsize=15)
    plt.show()