import gdspy
import numpy as np

# Function to generate the points for a parametric spiral
def parametric_spiral(resolution=1000):
    t = np.linspace(0, 6 * np.pi, resolution)
    x = np.exp(-0.1 * t) * np.cos(t)
    y = np.exp(-0.1 * t) * np.sin(t)
    return x, y

# Generate the spiral points
x, y = parametric_spiral()

# Create the path with the given line width
line_width = 1
spiral_path = gdspy.Path(line_width, (x[0], y[0]))

# Add points to the spiral path
for xi, yi in zip(x[1:], y[1:]):
    spiral_path.segment((xi, yi), final_width=line_width)

# Create a GDSII library and add the spiral path to it
gdsii_lib = gdspy.GdsLibrary()
cell = gdsii_lib.new_cell('SPIRAL')
cell.add(spiral_path)

# Save the library to a GDSII file
gdsii_lib.write_gds('spiral.gds')

print("The parametric spiral has been generated and saved to 'spiral.gds'.")