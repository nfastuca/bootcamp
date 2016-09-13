import numpy as np

def xa_to_diameter(xa):
    """
    Convert an array of cross-sectional areas to diameter
    """

    #compute diameter form area
    # A = pi d^2 / 4
    diameter = np.sqrt(xa *4 *np.pi)
    return diameter

A = np.array([[6.7, 1.3, 0.6, 0.7],
              [0.1, 5.5, 0.4, 2.4],
              [1.1, 0.8, 4.5, 1.7],
              [0.0, 1.5, 3.4, 7.5]])

b = np.array([1.1, 2.3, 3.3, 3.9])
