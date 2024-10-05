import gdspy

# Create a GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('CIRCLE_WITH_MARKERS')

# Draw the circle of radius 1600 um (3.2 mm diameter)
circle = gdspy.Round((0, 0), 1600)
cell.add(circle)

# Parameters for markers
R = 1600  # Radius of the circle in um
margin_x = 200  # Margin from the circle edge in x-direction
margin_y = 200  # Margin from the circle edge in y-direction

n_rows = 26       # Rows labeled A to Z
n_columns = 15    # Number of columns starting from 1

s_x = (2 * (R - margin_x)) / (n_columns - 1)  # Spacing in x-direction
s_y = (2 * (R - margin_y)) / (n_rows - 1)     # Spacing in y-direction

# Define marker size
marker_length = 100  # Total length of each arm of '+'
marker_width = 10    # Width of the lines

# Text label size
text_size = 30  # Size of text annotations

# Loop through grid positions
for i in range(n_columns):
    x = - (R - margin_x) + i * s_x
    for j in range(n_rows):
        y = - (R - margin_y) + j * s_y
        # Check if the point is within the circle
        if (x**2 + y**2) <= R**2:
            # Draw '+' sign at (x, y)
            # Vertical line
            vert_line = gdspy.Rectangle(
                (x - marker_width / 2, y - marker_length / 2),
                (x + marker_width / 2, y + marker_length / 2)
            )
            # Horizontal line
            horiz_line = gdspy.Rectangle(
                (x - marker_length / 2, y - marker_width / 2),
                (x + marker_length / 2, y + marker_width / 2)
            )
            cell.add([vert_line, horiz_line])

            # Add text annotations
            # Row label (A-Z)
            row_label = chr(ord('A') + j)
            # Column label (1 upwards)
            col_label = str(i + 1)

            # Place labels next to the marker
            # Place row label above the marker
            text_row = gdspy.Text(
                row_label,
                text_size,
                position=(x, y + marker_length / 2 + text_size),
                horizontal_alignment='center',
                vertical_alignment='bottom'
            )
            cell.add(text_row)
            # Place column label to the right of the marker
            text_col = gdspy.Text(
                col_label,
                text_size,
                position=(x + marker_length / 2 + text_size / 2, y),
                horizontal_alignment='left',
                vertical_alignment='center'
            )
            cell.add(text_col)

# Save the layout to a GDSII file
lib.write_gds('circle_with_markers.gds')

# Optionally, display the layout using the internal viewer