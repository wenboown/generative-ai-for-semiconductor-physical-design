import gdspy
import math

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('circle_with_fiducials')

# Define the circle parameters
circle_radius = 1.6  # 3.2 mm diameter
circle_center = (0, 0)

# Create the circle
circle = gdspy.Round(circle_center, circle_radius, layer=1)
cell.add(circle)

# Define the fiducial mark parameters
fiducial_size = 0.1  # 200 um
fiducial_margin = 0.2  # 200 um spacing between marks

# Calculate the number of fiducial marks in each row
num_rows = int(2 * circle_radius / fiducial_margin)
num_cols = int(2 * circle_radius / fiducial_margin)

# Create the fiducial marks and annotations
for row in range(-num_rows, num_rows + 1):
    for col in range(-num_cols, num_cols + 1):
        fiducial_center = (circle_center[0] + col * fiducial_margin, circle_center[1] + row * fiducial_margin)

        # Create the fiducial mark as a "+" sign
        fiducial_mark = gdspy.CellReference(gdspy.CellArray([gdspy.Rectangle(fiducial_center, 1.5 * fiducial_size, layer=2)]))
        fiducial_mark.translate(-0.5 * fiducial_size, -0.5 * fiducial_size)
        fiducial_mark.translate(fiducial_center[0], fiducial_center[1])
        cell.add(fiducial_mark)

        # Add horizontal line
        horizontal_line = gdspy.Rectangle((fiducial_center[0] - 0.5 * fiducial_size, fiducial_center[1]), (fiducial_center[0] + 0.5 * fiducial_size, fiducial_center[1]), layer=2)
        cell.add(horizontal_line)

        # Add vertical line
        vertical_line = gdspy.Rectangle((fiducial_center[0], fiducial_center[1] - 0.5 * fiducial_size), (fiducial_center[0], fiducial_center[1] + 0.5 * fiducial_size), layer=2)
        cell.add(vertical_line)

        # Add annotations
        annotation = chr(ord('A') + row + num_rows) + str(col + num_cols + 1)
        text = gdspy.Text(annotation, 0.05, fiducial_center, alignment='center', layer=3)
        cell.add(text)

# Save the design to a GDS file
lib.write_gds('circle_with_fiducials.gds')