import gdspy
import numpy as np

# Define the design specifications
circle_radius = 3.2 / 2 * 1000  # Convert mm to um
fiducial_length = 50  # um
fiducial_width = 5  # um
fiducial_spacing = 200  # um

# Create a new GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('circle_with_fiducials')

# Draw the circle
circle = gdspy.Round(center=(0, 0), radius=circle_radius, layer=1)
cell.add(circle)

# Calculate the number of fiducial marks in each row and column
num_rows = int(np.floor(circle_radius * 2 / fiducial_spacing))
num_cols = int(np.floor(circle_radius * 2 / fiducial_spacing))

# Create the fiducial marks and annotations
for row in range(-num_rows, num_rows + 1):
    for col in range(-num_cols, num_cols + 1):
        # Calculate the position of the fiducial mark
        x = col * fiducial_spacing
        y = row * fiducial_spacing

        # Draw the fiducial mark
        fiducial = gdspy.Path(nr_points=2, width=fiducial_width, layer=1)
        fiducial.segment([(x - fiducial_length / 2, y), (x + fiducial_length / 2, y)])
        fiducial.segment([(x, y - fiducial_length / 2), (x, y + fiducial_length / 2)])
        cell.add(fiducial)

        # Add annotation
        text = f"{chr(ord('A') + row)}{col + 1}"
        label = gdspy.Label(text, (x, y), layer=1)
        cell.add(label)

# Save the design to a GDS file
lib.write_gds('circle_with_fiducials.gds')