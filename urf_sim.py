import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import random
import cPickle


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
    total_applications = np.array([522, 529, 469, 330]).astype(float)
    female_applications = np.array([118, 132, 94, 66]).astype(float)

    total_shortlisted = np.array([123, 145, 127, 138]).astype(float)
    total_interviewed = np.array([63, 80, 68, 73]).astype(float)
    total_awards = np.array([30, 40, 37, 41]).astype(float)

    frac_women = np.mean(female_applications / total_applications)
    frac_shortlisted = np.mean(total_shortlisted / total_applications)
    frac_interviewed = np.mean(total_interviewed / total_shortlisted)
    frac_awards = np.mean(total_awards / total_interviewed)

    print frac_shortlisted, frac_interviewed, frac_awards, frac_women

    # now run simulation many times and get histogram
    all_women = []
    low = 0
    for i in range(1000):
        applicants = make_applicants(frac_women, 396)

        shortlisted = choose_urfs(applicants, frac_shortlisted, 0)
        interviewed = choose_urfs(shortlisted, frac_interviewed, 1)
        awarded = choose_urfs(interviewed, frac_awards, 2)
        n_women = get_women(awarded)
        all_women.append(n_women)
        if n_women <= 2:
            low += 1
        if i % 10 == 0:
            print i, len(awarded), n_women
    mn = np.mean(all_women)
    std = np.std(all_women)
    p_2 = stats.norm.pdf(2, loc=mn, scale=std)
    print mn, std, p_2, low

    # save data
    with open("women.pkl", "w") as f:
        cPickle.dump(all_women, f)

if __name__ == "__main__":
    main()