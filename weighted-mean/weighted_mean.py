import numpy as np

def weighted_mean_solver(values, uncertainties):

    weights = 1/(uncertainties)**2

    weighted_mean = np.sum(weights * values) / np.sum(weights)

    return weighted_mean

