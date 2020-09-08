import math
import matplotlib.pyplot as plt

print("Hello world")


# Return the likelihood of a value given parameters of a gaussian.
def get_likelihood(value, mu, sigma):
    # I know there are ways to just directly get the likelihood from some python librarie, but this does it
    # explicitly
    return (1 / math.sqrt(2 * math.pi * sigma ** 2)) * math.exp(-1 * ((value - mu) ** 2) / (2 * sigma ** 2))


# Background stuff
mu_b = 0
mu_p = 50
prior_b = 0.75
prior_p = 0.25

# Part a (note, we convert the sigma squared to just the sigma values
s_b = 12
s_p = 12


def get_prob(v, m1, m2, s1, s2, p1, p2):
    likelihood_1 = get_likelihood(v, m1, s1)
    likelihood_2 = get_likelihood(v, m2, s2)
    return likelihood_1 * p1 / (likelihood_1 * p1 + likelihood_2 * p2)


# In part a, get a time of 25 ms
val = 25
prob_p = get_prob(val, mu_p, mu_b, s_p, s_b, prior_p, prior_b)
# Print out computed value; should equal 0.25
print("Probability that it was p is", prob_p)
# Extra credit for part a: varying the value
vals = [-25, 0, 25, 50, 75]
prob_values = [get_prob(val, mu_p, mu_b, s_p, s_b, prior_p, prior_b) for val in vals]
plt.bar(vals, prob_values, width=20)
plt.title("Probability of p given VOT part a")
plt.show()


######################## Part B ###########################
# Change the variances of the two distributions
s_b = 8
s_p = 12
# Extra credit for part b: varying the value
vals = [-25, 0, 25, 50, 75]
prob_values = [get_prob(val, mu_p, mu_b, s_p, s_b, prior_p, prior_b) for val in vals]
plt.bar(vals, prob_values, width=20)
plt.title("Probability of p given VOT part b")
plt.show()


######################## Part C ###########################
# Using same parameters as b, but extend range of VOTs hugely.
# Extra credit for part c: varying the value
vals = [-200, -150, -100, -50, -25, 0, 25, 50, 75]
prob_values = [get_prob(val, mu_p, mu_b, s_p, s_b, prior_p, prior_b) for val in vals]
plt.bar(vals, prob_values, width=20)
plt.title("Probability of p given VOT part c")
plt.show()
