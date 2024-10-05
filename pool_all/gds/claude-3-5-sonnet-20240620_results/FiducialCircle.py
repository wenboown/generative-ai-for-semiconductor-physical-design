import gdspy
import numpy as np

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('FIDUCIAL_CIRCLE')

# Define parameters
circle_diameter = 3200  # 3.2 mm in μm
circle_radius = circle_diameter / 2
fiducial_size = 50  # 50 μm
fiducial_spacing = 200  # 200 μm
annotation_size = 50  # 50 μm

# Create the main circle
circle = gdspy.Round((0, 0), circle_radius, tolerance=0.1)
cell.add(circle)

# Create fiducial marks and annotations
rows = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cols = range(1, 27)

for i, row in enumerate(rows):
    for j, col in enumerate(cols):
        x = (j - 13) * fiducial_spacing
        y = (12 - i) * fiducial_spacing
        
        # Check if the fiducial is inside the circle
        if x**2 + y**2 <= circle_radius**2:
            # Create the "+" fiducial mark
            horizontal = gdspy.Rectangle((x - fiducial_size/2, y - fiducial_size/10),
                                         (x + fiducial_size/2, y + fiducial_size/10))
            vertical = gdspy.Rectangle((x - fiducial_size/10, y - fiducial_size/2),
                                       (x + fiducial_size/10, y + fiducial_size/2))
            fiducial = gdspy.boolean(horizontal, vertical, 'or')
            cell.add(fiducial)
            
            # Add annotation
            label = f'{row}{col}'
            text = gdspy.Text(label, annotation_size, (x + fiducial_size, y - fiducial_size))
            cell.add(text)

# Save the design to a GDS file
lib.write_gds('fiducial_circle.gds')