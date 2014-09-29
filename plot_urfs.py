import cPickle
import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np

def main():
    py.sign_in('rebecca_roisin', 'ay9gikxvge')

    # load simulated data
    with open("women_bias.pkl", "r") as f:
        all_women = cPickle.load(f)

    tot = 0

    for b, women in all_women.iteritems():
    
        # plot histogram
        fig = plt.figure()
        ax = plt.subplot(111)

        ax.hist(women, bins=np.arange(0, max(women)+1, 1), normed=True, histtype="step", label="bias: %s" % b)
    ax.set_xlabel("Number of Women")
    ax.set_ylabel("Frequency")

    plot_url = py.plot_mpl(fig)
    plt.show()

if __name__ == "__main__":
    main()
