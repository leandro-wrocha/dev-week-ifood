import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import constants.index as constants

class GenerateGraphicsNPS:
    def __init__(self, nps):
        self.nps = nps
        self.NPS_ZONES = constants.NPS_ZONES
        self.NPS_VALUES = constants.NPS_VALUES
        self.NPS_COLORS = constants.NPS_COLORS

    def get_nps(self):
        return self.nps

    def execute(self):
        nps = self.get_nps()
        fig, ax = plt.subplots(figsize=(10, 2))

        for index, zone in enumerate(self.NPS_ZONES):
            ax.barh(
                [0],
                width=self.NPS_VALUES[index + 1] - self.NPS_VALUES[index],
                left=self.NPS_VALUES[index],
                color=self.NPS_COLORS[index]
            )

        ax.barh([0], width=1, left=nps, color='black')
        ax.set_yticks([])
        ax.set_xlim(-100, 100)
        ax.set_xticks(self.NPS_VALUES)

        plt.text(nps, 0, f'{nps:.2f}', ha='center', va='center', color='white', bbox=dict(facecolor='black'))

        patches = [mpatches.Patch(color=self.NPS_COLORS[index], label=self.NPS_ZONES[index]) for index in range(len(self.NPS_ZONES))]
        plt.legend(handles=patches, bbox_to_anchor=(0,1))

        plt.show()
