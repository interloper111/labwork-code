import numpy as np
from weighted_mean import weighted_mean_solver
from weighted_uncertainty import weighted_uncertainty_solver

data = np.genfromtxt("data.txt",dtype='float',delimiter=',',skip_header=0)

values = data[:, 0]
uncertainties = data[:, 1]

weighted_mean= weighted_mean_solver(values, uncertainties)
weighted_uncertainty = weighted_uncertainty_solver(uncertainties)

print(f"{weighted_mean} ± {weighted_uncertainty}")