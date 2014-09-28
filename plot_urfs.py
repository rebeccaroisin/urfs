import cPickle
import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np

def main():
    py.sign_in('rebecca_roisin', 'ay9gikxvge')

    # load simulated data
    with open("women.pkl", "r") as f:
        all_women = cPickle.load(f)

    # plot histogram
    fig = plt.figure()
    ax = plt.subplot(111)

    ax.hist(all_women, bins=np.arange(0, max(all_women)+1, 1), normed=True)
    ax.set_xlabel("Number of Women")
    ax.set_ylabel("Frequency")

    plot_url = py.plot_mpl(fig)
    plt.show()

if __name__ == "__main__":
    main()
