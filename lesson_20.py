import numpy as np

def xa_to_diameter(xa):
    """
    Convert an array of cross-sectional areas to diameter
    """

    #compute diameter form area
    # A = pi d^2 / 4
    diameter = np.sqrt(xa *4.np.pi)
    
