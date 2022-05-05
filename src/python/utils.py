import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class Utils:
    @staticmethod
    def multiline_plot(fig_size, title, x_axis_label, xs, y_axis_label, y_legends, yss):
        fig = plt.figure(figsize = fig_size)

        for i, ys in enumerate(yss):
            ax = sns.lineplot(label=y_legends[i], x=xs, y=ys)

        ax.set_xlim(0, len(xs))
        ax.set_title(title, fontsize=14)
        ax.set_ylabel(y_axis_label, fontsize=14)
        ax.set_xlabel(x_axis_label, fontsize=14)
        ax.set_xticks(range(0, len(xs), len(xs) // 25))

        plt.legend(fontsize='x-large')
        plt.tight_layout() 
        plt.show();