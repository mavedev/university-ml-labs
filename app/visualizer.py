import matplotlib.pyplot as plt
import pandas as pd

from singletons import Singleton

import app.invariants as invariants
import app.types as types


class Visualizer(metaclass=Singleton):
    @staticmethod
    def show(filepath: types.Path) -> None:
        cvs_content = pd.read_csv(filepath)
        fig, axes = plt.subplots(
            nrows=7, ncols=2, figsize=(15, 20), dpi=80,
            facecolor='w', edgecolor='k'
        )

        for i in range(len(invariants.feature_keys)):
            key = invariants.feature_keys[i]
            color = invariants.colors[i % (len(invariants.colors))]
            t_data = cvs_content[key]
            t_data.index = cvs_content[invariants.date_time_key]
            t_data.head()
            ax = t_data.plot(
                ax=axes[i // 2, i % 2],
                color=color,
                title=f'{invariants.titles[i]} - {key}',
                rot=25,
            )
            ax.legend([invariants.titles[i]])

        plt.tight_layout()
