import gdspy
import numpy as np

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Create a cell in the library
cell = lib.new_cell('CIRCLE_WITH_FIDUCIALS')

# Define the circle parameters
circle_radius = 3.2e3 / 2  # Circle radius in micrometers
origin = (0, 0)  # Circle center

# Create the circle
circle = gdspy.Round(origin, circle_radius, tolerance=0.01)
cell.add(circle)

# Fiducial mark parameters
marker_length = 200  # micrometers
spacing = 200 / 2  # Half value for easy placement

# Generate row labels and column numbers
rows = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
columns = [str(i) for i in range(1, 27)]  # 26 columns

# Place fiducial marks with annotations
fiducial_positions = []

# Determine fiducial placement
for i, row in enumerate(rows):
    for j, col in enumerate(columns):
        # Positioning each fiducial marker
        x_pos = j * spacing
        y_pos = -i * spacing
        
        if np.hypot(x_pos, y_pos) > circle_radius:
            continue
        
        # Create horizontal bar of fiducial
        fiducial_h = gdspy.Rectangle((x_pos - marker_length / 2, y_pos - marker_length / 20),
                                     (x_pos + marker_length / 2, y_pos + marker_length / 20))
        # Create vertical bar of fiducial
        fiducial_v = gdspy.Rectangle((x_pos - marker_length / 20, y_pos - marker_length / 2),
                                     (x_pos + marker_length / 20, y_pos + marker_length / 2))
        cell.add(fiducial_h)
        cell.add(fiducial_v)
        
        # Add an annotation
        label = f'{row}{col}'
        text_label = gdspy.Text(label, 50, (x_pos + marker_length / 2 + 50, y_pos - 25))
        cell.add(text_label)

# Save the library to a file
lib.write_gds('circle_with_fiducials.gds')

# Display the layout in the viewer