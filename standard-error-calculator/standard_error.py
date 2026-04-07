import numpy as np

def find_standard_errors(matrix):
    
    # Finds standard deviation for each row (uses n−1)
    standard_deviation = np.std(matrix, axis=1, ddof=1)
    
    # Number of values per row
    n = matrix.shape[1]
    
    # Standard error of the mean (SEM)
    standard_error = standard_deviation / np.sqrt(n)
     
    return standard_error
