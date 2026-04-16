import numpy as np
import matplotlib.pyplot as plt

class EbbinghausForgettingCurve:
    def __init__(self, time_periods):
        self.time_periods = time_periods

    def forget(self):
        intervals = np.array(self.time_periods)
        retention = np.exp(-0.1 * intervals)
        return retention

    def plot_curve(self):
        retention = self.forget()
        plt.plot(self.time_periods, retention, marker='o')
        plt.title('Ebbinghaus Forgetting Curve')
        plt.xlabel('Time (Days)')
        plt.ylabel('Retention (%)')
        plt.xticks(self.time_periods)
        plt.grid()
        plt.show()

# Example usage:
if __name__ == '__main__':
    time_periods = [0, 1, 2, 7, 14, 30]  # Days after learning
    forgetting_curve = EbbinghausForgettingCurve(time_periods)
    forgetting_curve.plot_curve()