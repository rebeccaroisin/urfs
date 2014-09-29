import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import random
import cPickle
import plotly.plotly as py


def make_applicants(f_women, total):
    # list to hold applicants
    applicants = []
    for app in range(total):
        # global score = overall ability
        global_score = stats.norm.rvs(loc=50, scale=20)

        # s1-3: performance at 3 application stages
        s1 = stats.norm.rvs(loc=global_score, scale=20)
        s2 = stats.norm.rvs(loc=global_score, scale=20)
        s3 = stats.norm.rvs(loc=global_score, scale=20)

        # gender of applicant
        gender = random.random()
        if gender <= f_women:
            applicants.append((s1, s2, s3, "F")) # female
        else:
            applicants.append((s1, s2, s3, "N")) # not female
    return applicants

def make_biased_applicants(f_women, total, bias=0):
    # list to hold applicants
    applicants = []
    for app in range(total):
        # gender of applicant
        gender = random.random()
        if gender <= f_women:
            # global score = overall ability
            # reduce the score for women by some bias value
            global_score = stats.norm.rvs(loc=50-bias, scale=5)

            # s1-3: performance at 3 application stages
            s1 = stats.norm.rvs(loc=global_score, scale=5)
            s2 = stats.norm.rvs(loc=global_score, scale=5)
            s3 = stats.norm.rvs(loc=global_score, scale=5)

            applicants.append((s1, s2, s3, "F")) # female
        else:
            global_score = stats.norm.rvs(loc=50, scale=5)

            # s1-3: performance at 3 application stages
            s1 = stats.norm.rvs(loc=global_score, scale=5)
            s2 = stats.norm.rvs(loc=global_score, scale=5)
            s3 = stats.norm.rvs(loc=global_score, scale=5)

            applicants.append((s1, s2, s3, "N")) # not female
    return applicants


def choose_urfs(applicants, f_selected, stage):
    applicants = sorted(applicants, key=lambda x: x[stage], reverse=True)
    n_selected = int(f_selected * len(applicants))
    selected = applicants[:n_selected+1]
    return selected

def get_women(candidates):
    women = 0
    for cand in candidates:
        if cand[-1] == "F":
            women += 1
    return women

def main():
    # get statistics
    total_applications = np.array([522, 529, 469, 330, 396]).astype(float)
    female_applications = np.array([118, 132, 94, 66, 75]).astype(float)

    total_shortlisted = np.array([123, 145, 127, 138, 126]).astype(float)
    total_interviewed = np.array([63, 80, 68, 73, 68]).astype(float)
    total_awards = np.array([30, 40, 37, 41, 43]).astype(float)

    frac_women = np.mean(female_applications[-1] / total_applications[-1])
    frac_shortlisted = np.mean(total_shortlisted / total_applications)
    frac_interviewed = np.mean(total_interviewed / total_shortlisted)
    frac_awards = np.mean(total_awards / total_interviewed)

    print frac_shortlisted, frac_interviewed, frac_awards, frac_women

    # now run simulation many times and get histogram
    all_women = {}
    low = 0

    # plot histogram
    fig = plt.figure()
    ax = plt.subplot(111)

    for b in np.arange(2, 12, 2):
        women = []
        for i in range(1000):
            applicants = make_biased_applicants(frac_women, 396, bias=b)

            shortlisted = choose_urfs(applicants, frac_shortlisted, 0)
            interviewed = choose_urfs(shortlisted, frac_interviewed, 1)
            awarded = choose_urfs(interviewed, frac_awards, 2)
            n_women = get_women(awarded)
            women.append(n_women)
            if n_women <= 2:
                low += 1
            if i % 10 == 0:
                print i, len(awarded), n_women
        mn = np.mean(women)
        std = np.std(women)
        p_2 = stats.norm.pdf(2, loc=mn, scale=std)
        all_women[b] = women
        print mn, std, p_2, low


        ax.hist(women, bins=np.arange(0, max(women)+1, 1), normed=True, histtype="step", label="bias: %s" % b)
    ax.set_xlabel("Number of Women")
    ax.set_ylabel("Frequency")
    ax.legend()

    #plot_url = py.plot_mpl(fig)
    plt.savefig("bias.png")
    plt.show()


    # save data
    with open("women_bias.pkl", "w") as f:
        cPickle.dump(all_women, f)

if __name__ == "__main__":
    main()