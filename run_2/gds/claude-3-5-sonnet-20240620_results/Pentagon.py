import gdspy
import numpy as np

# Calculate the coordinates of a regular pentagon
def calculate_pentagon_coordinates(side_length):
    angle = 2 * np.pi / 5  # Internal angle of the pentagon in radians
    radius = side_length / (2 * np.sin(np.pi / 5))  # Radius of the circumscribed circle
    
    coordinates = []
    for i in range(5):
        x = radius * np.cos(i * angle)
        y = radius * np.sin(i * angle)
        coordinates.append((x, y))
    
    return coordinates

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('PENTAGON')

# Define the side length (10 mm = 10000 µm)
side_length = 10000  # in µm

# Calculate pentagon coordinates
pentagon_coords = calculate_pentagon_coordinates(side_length)

# Create the pentagon polygon
pentagon = gdspy.Polygon(pentagon_coords)

# Add the pentagon to the cell
cell.add(pentagon)

# Center the pentagon at (0, 0)
cell.center = (0, 0)

# Save the GDSII file
lib.write_gds('pentagon.gds')

print("Pentagon GDS file has been generated successfully.")