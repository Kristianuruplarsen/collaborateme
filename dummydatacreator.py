import numpy as np

def create_dummy_data(n_vars, n_rows=10000):
    """Creates linearly independent dummy data, made for testing ML algs.

    Parameters
    ==========
    n_vars : (int)
        number of variables
    rows : (int)
        number of rows


    returns
    =======
    X : features
        np.array with N_rows times n_vars N(0,1) vars
    y : target
        np.array with N_rows entries. (dot product of params and X)
    params : parameters for dot product
        np.array with n_vars entries.
    """

    params = np.array([np.random.normal() for i in range(n_vars)])

    X = np.random.normal(size=(n_rows, n_vars))
    y = np.dot(X, params)

    return X, y, params
