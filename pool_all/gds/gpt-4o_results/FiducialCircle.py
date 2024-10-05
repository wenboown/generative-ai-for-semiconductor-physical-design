import gdspy
import numpy as np

# Initialize the GDS Library and Layout Cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('CIRCLE_WITH_FIDUCIALS')

# Circle parameters
circle_radius = 3.2e3 / 2  # Radius in micrometers (3.2 mm diameter)
circle_origin = (0, 0)

# Create the main circle
circle = gdspy.Round(circle_origin, circle_radius)
cell.add(circle)

# Fiducial parameters
marker_length = 100  # Fiducial marker length (half length = 50 um)
fiducial_spacing = 200  # Fiducial spacing

# Annotations
rows = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
columns = range(1, 14)  # Limited to 13 for simplicity

# Create fiducials and add annotations
for i, row in enumerate(rows):
    for j, col in enumerate(columns):
        x = (j - len(columns) // 2) * fiducial_spacing
        y = (len(rows) // 2 - i) * fiducial_spacing
        
        # Check if within the circle
        if np.hypot(x, y) + marker_length / 2 > circle_radius:
            continue

        # Create the "+" sign as two rectangles
        horizontal = gdspy.Rectangle((x - marker_length / 2, y - 10), 
                                     (x + marker_length / 2, y + 10))
        vertical = gdspy.Rectangle((x - 10, y - marker_length / 2), 
                                   (x + 10, y + marker_length / 2))
        cell.add(horizontal)
        cell.add(vertical)

        # Add annotation
        annotation = f'{row}{col}'
        text = gdspy.Text(str(annotation), 50, (x + marker_length / 2 + 20, y - 20))
        cell.add(text)

# Save the design to a GDS file
lib.write_gds('circle_with_fiducials.gds')