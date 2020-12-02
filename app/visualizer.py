import matplotlib.pyplot as plt
import pandas as pd

from singletons import Singleton

from .invariants import Constants, Types


class Visualizer(metaclass=Singleton):
    @staticmethod
    def show(filepath: Types.Path) -> None:
        cvs_content = pd.read_csv(filepath)
        fig, axes = plt.subplots(
            nrows=7, ncols=2, figsize=(15, 20), dpi=80,
            facecolor='w', edgecolor='k'
        )

        for i in range(len(Constants.FEATURE_KEYS)):
            key = Constants.FEATURE_KEYS[i]
            color = Constants.COLORS[i % (len(Constants.COLORS))]
            t_data = cvs_content[key]
            t_data.index = cvs_content[Constants.DATE_TIME_KEY]
            t_data.head()
            ax = t_data.plot(
                ax=axes[i // 2, i % 2],
                color=color,
                title=f'{Constants.TITLES[i]} - {key}',
                rot=25,
            )
            ax.legend([Constants.TITLES[i]])

        plt.tight_layout()
