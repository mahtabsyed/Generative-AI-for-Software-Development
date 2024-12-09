# Prompt: Can you add docstring in Google style includng example usage and inline doc for this function intended for an experienced develeoper

import numpy as np
def sphere_volume(radius):
    """
    Calculate the volume of a sphere given its radius.

    The formula for the volume of a sphere is (4/3) * π * r^3.

    Parameters:
    radius (float): The radius of the sphere.

    Returns:
    float: The volume of the sphere.

    Example:
    >>> 
    >>> sphere_volume(3)
    113.09733552923254
    """
    return (4 / 3) * np.pi * radius**3

print(sphere_volume(3)) # 113.09733552923254