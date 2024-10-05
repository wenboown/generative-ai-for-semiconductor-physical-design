import gdspy
import numpy as np

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("fiducial_marks")

# Define the circle parameters
circle_radius = 3.2e3  # 3.2 mm in microns
circle = gdspy.Round(
    (0, 0), circle_radius, number_of_points=128
)  # Create a circle with high point density for smoothness

# Add the circle to the cell
cell.add(circle)

# Define the fiducial mark parameters
marker_length = 200  # 200 um
marker_width = 20  # 20 um
marker_spacing = 200  # 200 um
annotation_font_size = 100  # 100 um

# Calculate the number of rows and columns
max_row_col = int(np.floor(2 * circle_radius / marker_spacing))
num_rows = int(max_row_col)
num_cols = int(max_row_col)

# Create the fiducial marks and annotations
for i in range(num_rows):
    for j in range(num_cols):
        # Calculate the marker position
        x = (j - (num_cols - 1) / 2) * marker_spacing
        y = (i - (num_rows - 1) / 2) * marker_spacing

        # Create the marker
        marker = gdspy.Rectangle(
            (x - marker_length / 2, y - marker_width / 2),
            (x + marker_length / 2, y + marker_width / 2),
            layer=1,
        )
        marker2 = gdspy.Rectangle(
            (x - marker_width / 2, y - marker_length / 2),
            (x + marker_width / 2, y + marker_length / 2),
            layer=1,
        )
        cell.add(marker)
        cell.add(marker2)

        # Create the annotation
        row_label = chr(ord("A") + i)
        col_label = str(j + 1)
        label = row_label + col_label
        text = gdspy.Text(
            label, annotation_font_size, (x, y + marker_length / 2 + 20)
        )
        cell.add(text)

# Save the design to a GDS file
lib.write_gds("fiducial_marks.gds")