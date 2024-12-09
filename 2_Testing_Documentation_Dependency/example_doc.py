# Can you review the inline comments in this code snippet and imporve by following the best practices for inline comments?
# inline comments
import pandas as pd
import numpy as np

# Load weather data from CSV file into a DataFrame
weather_df = pd.read_csv('april2024_station_data.csv')

# Convert wind speed and direction columns to numpy arrays for faster computation
wind_speed = weather_df['wind_speed'].to_numpy()
wind_direction = weather_df['wind_direction'].to_numpy()

# Convert wind direction from degrees to radians using numpy's built-in function
wind_direction_rad = np.deg2rad(wind_direction)


# Write a function to calculate volume of a sphere
# Prompt: Can you add examples to call this function in docstring


def sphere_volume(radius):
    """
    Calculate the volume of a sphere given its radius.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The volume of the sphere.

    Examples:
        >>> sphere_volume(1)
        4.1887902047863905

        >>> sphere_volume(3)
        113.09733552923254
    """
    return (4 / 3) * np.pi * radius**3
