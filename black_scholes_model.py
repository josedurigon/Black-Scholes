#implementation of black and scholes formula
import numpy as np

# Variables
r = float(input("Free risk rate: "))
s = float(input("Subjacent equity price: "))
k = float(input("Option strike price: "))
t = float(input("Time till default in days (just put the number please thx): "))
t = t / 365
sigma = float(input("Volatility (that you should have calculated mate): "))
option_type = input("CALL[C] or PUT[P]: ").upper()

def cumulative_normal_distribution(x):
    return (1.0 + np.math.erf(x / np.sqrt(2.0))) / 2.0

def calculate_implied_volatility(r, s, k, t, price, option_type="C"):
    # Implementar o cálculo da volatilidade implícita
    # usando métodos iterativos, como o método de Newton ou o método de bisseção.
    # Retornar a volatilidade implícita calculada
    pass

def calculate_delta(r, s, k, t, sigma, option_type="C"):
    d1 = (np.log(s / k) + (r + sigma ** 2 / 2) * t) / (sigma * np.sqrt(t))

    if option_type == "C":
        delta = cumulative_normal_distribution(d1)
    elif option_type == "P":
        delta = cumulative_normal_distribution(d1) - 1

    return delta

def calculate_gama(r, s, k, t, sigma):
    d1 = (np.log(s / k) + (r + sigma ** 2 / 2) * t) / (sigma * np.sqrt(t))
    gama = cumulative_normal_distribution(d1) / (s * sigma * np.sqrt(t))
    return gama

def calculate_vega(r, s, k, t, sigma):
    d1 = (np.log(s / k) + (r + sigma ** 2 / 2) * t) / (sigma * np.sqrt(t))
    vega = s * np.sqrt(t) * np.exp(-d1 ** 2 / 2) / np.sqrt(2 * np.pi)
    return vega


def blackScholes(r, s, k, t, sigma, option_type="C"):
    d1 = (np.log(s / k) + (r + sigma ** 2 / 2) * t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)

    try:
        if option_type == "C":
            price = s * cumulative_normal_distribution(d1) - k * np.exp(-r * t) * cumulative_normal_distribution(d2)
        elif option_type == "P":
            price = k * np.exp(-r * t) * cumulative_normal_distribution(-d2) - s * cumulative_normal_distribution(-d1)
        return price
    except:
        print("Please confirm all options parameters above...")

option_price = blackScholes(r, s, k, t, sigma, option_type=option_type)
print("Option Price is:", round(option_price, 2))

