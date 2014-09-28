import matplotlib.pyplot as plt
import matplotlib
import plotly.plotly as py
import numpy as np


def main():
	py.sign_in('rebecca_roisin', 'ay9gikxvge')

	matplotlib.rcParams.update({'font.size': 10})


	# raw data -- copied in by hand
	year = np.array([2010, 2011, 2012, 2013, 2014])

	total_applications = np.array([522, 529, 469, 330, 396]).astype(float)
	female_applications = np.array([118, 132, 94, 66, 75]).astype(float)

	total_shortlisted = np.array([123, 145, 127, 138, 126]).astype(float)
	female_shortlisted = np.array([33, 31, 18, 29, 17]).astype(float)

	total_interviewed = np.array([63, 80, 68, 73, 68]).astype(float)
	female_interviewed = np.array([18, 20, 12, 16, 6]).astype(float)

	total_awards = np.array([30, 40, 37, 41, 43]).astype(float)
	female_awards = np.array([10, 7, 7, 7, 2]).astype(float)


	# data processing
	# assume gender binary
	male_applications = total_applications - female_applications
	male_shortlisted = total_shortlisted - female_shortlisted
	male_interviewed = total_interviewed - female_interviewed
	male_awards = total_awards - female_awards

	# fraction female
	frac_applications = female_applications / total_applications
	frac_shortlisted = female_shortlisted / total_shortlisted
	frac_interviewed = female_interviewed / total_interviewed
	frac_awards = female_awards / total_awards

	# success probability
	# women
	shortlist_fp = female_shortlisted / female_applications
	interview_fp = female_interviewed / female_shortlisted
	award_fp = female_awards / female_interviewed

	# men
	shortlist_mp = male_shortlisted / male_applications
	interview_mp = male_interviewed / male_shortlisted
	award_mp = male_awards / male_interviewed

	# fraction of applicants
	frac_female = female_applications / total_applications
	frac_male = male_applications / total_applications


	# fraction of awards to women
	frac_fem_award = female_awards / total_awards

	# make plot


	fig = plt.figure()
	ax = plt.subplot(111)
	#ax.get_major_formatter().set_useOffset(False)

	ax.plot(year, frac_fem_award, label="female", color="b")
	#ax.plot(year, frac_female, label="female", color="b")
	#ax.plot(year, frac_male, label="male", color="g")

	#ax.plot(year, shortlist_mp, label="shortlist male", color="r", linestyle="--")
	#ax.plot(year, interview_fp, label="interview female", color="b")
	#ax.plot(year, interview_mp, label="interview male", color="b", linestyle="--")
	#ax.plot(year, award_fp, label="award female", color="g")
	#ax.plot(year, award_mp, label="award male", color="g", linestyle="--")
	#plt.plot(year,frac_shortlisted, label="shortlisted")
	#plt.plot(year,frac_interviewed, label="interviewed")
	#plt.plot(year,frac_awards, label="awards")
	#plt.scatter(year, women)
	ax.set_xlim(2010, 2014)
	ax.set_xticks([2010, 2011, 2012, 2013, 2014])
	ax.set_ylim(0, 1)
	ax.set_xlabel("Year")
	ax.set_ylabel("Probability")
	ax.set_title("Awards to Women") 
	#ax.legend(loc="upper right")

	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
	                 box.width, box.height * 0.9])

	# Put a legend below current axis
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
	          fancybox=True, shadow=True, ncol=3)
	#plt.savefig("women.pdf")
	#plt.savefig("women.png")
	plot_url = py.plot_mpl(fig)
	plt.show()

if __name__ == "__main_":
	main()