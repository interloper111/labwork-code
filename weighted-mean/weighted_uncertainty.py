import numpy as np

def weighted_uncertainty_solver(uncertainties):

    weights = 1/(uncertainties)**2

    weighted_uncertainty = np.sqrt(1.0 / np.sum(weights))

    return weighted_uncertainty