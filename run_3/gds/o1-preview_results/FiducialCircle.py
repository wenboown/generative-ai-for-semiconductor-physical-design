import gdspy
import string

# Create a GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('CIRCLE_WITH_FIDUCIALS')

# Circle parameters
circle_radius = 1600  # µm (since diameter is 3200 µm)
circle_center = (0, 0)

# Draw the circle
circle = gdspy.Round(circle_center, circle_radius, number_of_points=256, layer=1)
cell.add(circle)

# Fiducial mark parameters
spacing = 200  # µm between the centers of the markers
marker_size = 50  # µm (half-length of '+' arms)
marker_width = 10  # µm (width of '+' arms)
start_x = -1400  # Starting x position for markers
start_y = -1400  # Starting y position for markers
num_rows = 26  # Number of rows (A to Z)
num_cols = int((2800 / spacing) + 1)  # Calculate number of columns based on spacing

# Letters for row annotations
row_labels = list(string.ascii_uppercase)

# Loop over grid positions
for j in range(num_rows):
    for i in range(num_cols):
        x = start_x + i * spacing
        y = start_y + j * spacing
        # Check if the point is within the circle
        if (x - circle_center[0])**2 + (y - circle_center[1])**2 <= circle_radius**2:
            # Draw '+' sign
            # Vertical line of '+'
            vertical_line = gdspy.Rectangle(
                (x - marker_width / 2, y - marker_size),
                (x + marker_width / 2, y + marker_size),
                layer=2
            )
            # Horizontal line of '+'
            horizontal_line = gdspy.Rectangle(
                (x - marker_size, y - marker_width / 2),
                (x + marker_size, y + marker_width / 2),
                layer=2
            )
            cell.add([vertical_line, horizontal_line])
            # Add annotation next to marker
            row_label = row_labels[j % len(row_labels)]
            col_label = str(i + 1)
            text_label = f"{row_label}{col_label}"
            text = gdspy.Text(
                text_label,
                70,
                (x + marker_size + 20, y + marker_size + 20),
                layer=3
            )
            cell.add(text)

# Save the GDSII file
lib.write_gds('circle_with_fiducials.gds')