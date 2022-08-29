#implement black and scholes formula
import numpy as np
from scipy.stats import norm

#variables
r = 0.1375
s = 30
k = 40
t = 240/365
sigma = 0.30

def blackScholes(r,s,k,t,sigma, type="C"):
    d1=(np.log(s/k)+(r+sigma**2/2)*t)/(sigma*np.sqrt(t))
    d2= d1 - sigma *np.sqrt(t)

    try:
        if type =="C":
            price = s*norm.cdf(d1,0,1)- k*np.exp(-r*t)*norm.cdf(d2,0,1)

        elif type=="C":
            price = k*np.exp(-r*t)*norm.cdf(-d2,0,1)-s*norm.cdf(-d1,0,1)
        return price
    except:
        print("Please confirm all options parameters above...")
    
print("Option Price is: ", round(blackScholes(r,s,k,t,sigma, type="C"),2))
