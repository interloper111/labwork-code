import numpy as np
from standard_error import find_standard_errors

# Takes data from data.txt and converts it to a matrix (assumes no header and data is separated by a comma)
data = np.genfromtxt("data.txt",dtype='float',delimiter=',',skip_header=0)

# Prints list of standard errors
print(find_standard_errors(data))
