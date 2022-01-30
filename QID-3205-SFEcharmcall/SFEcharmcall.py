import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt
from matplotlib import cm

# parameter settings
save_figure = True
S_min = 50          # lower bound of Asset Price
S_max = 150         # upper bound of Asset Price
tau_min = 0.05      # lower bound of Time to Maturity
tau_max = 1         # upper bound of Time to Maturity
K = 100             # exercise price
r = 0.1             # riskfree interest rate
sig = 0.35          # volatility
d = 0.2             # dividend rate
steps = 60          # steps

tau = np.linspace(tau_min, tau_max, steps)
S = np.linspace(S_max, S_min, steps)


def get_charmcall(tau, S, K, r, d, sig):
    y = (np.log(S/K) + (r - d - sig**2/2) * tau)/(sig * np.sqrt(tau))
    d1 = y+sig*np.sqrt(tau)

    return -np.exp(-d*tau)*(norm.pdf(d1)*((r-d)/(sig*np.sqrt(tau))-y/(2*tau))-d*norm.cdf(d1))

X, Y = np.meshgrid(tau, S)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, get_charmcall(X, Y, K, r, d, sig), cmap=cm.viridis)
ax.set_title('Dependence of Charm on Stock Price and Time to Maturity')
ax.set_xlabel('Time to Maturity')
ax.set_ylabel('Stock Price')
ax.set_zlabel('Charm')
plt.show()

if save_figure:
    fig.savefig('SFEcharmcall.png', transparent=True)
