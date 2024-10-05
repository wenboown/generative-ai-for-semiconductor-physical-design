import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('FIDUCIAL_MARKS')

# Draw a circle of diameter 3.2 mm
circle_diameter = 3200  # 3.2 mm in micrometers
circle_radius = circle_diameter / 2  # Radius in micrometers

# Create the circle
circle = gdspy.Round((0, 0), circle_radius, number_of_points=0.01)
cell.add(circle)

# Parameters for fiducial marks
marker_spacing = 200       # Spacing between markers in micrometers
marker_size = 100          # Size of the '+' marker in micrometers
marker_thickness = 10      # Line thickness of the '+' marker in micrometers

# Calculate the number of markers that can fit in x and y directions
num_rows = int((2 * circle_radius) // marker_spacing) + 1
num_rows = min(num_rows, 26)  # Limit to 26 rows (A-Z)
num_cols = num_rows           # Assuming a square grid

# Generate y positions for the rows
y_positions = [(-circle_radius + i * marker_spacing) for i in range(num_rows)]
x_positions = [(-circle_radius + i * marker_spacing) for i in range(num_cols)]

# Row labels from A to Z
row_labels = [chr(ord('A') + i) for i in range(num_rows)]

# Generate fiducial marks and annotations
for row_index, y in enumerate(y_positions):
    col_index = 0
    for x in x_positions:
        # Check if the marker is within the circle boundary
        if x**2 + y**2 <= (circle_radius - marker_size)**2:
            # Create the '+' marker
            hor_line = gdspy.Rectangle(
                (x - marker_size / 2, y - marker_thickness / 2),
                (x + marker_size / 2, y + marker_thickness / 2)
            )
            ver_line = gdspy.Rectangle(
                (x - marker_thickness / 2, y - marker_size / 2),
                (x + marker_thickness / 2, y + marker_size / 2)
            )
            plus_sign = gdspy.boolean(hor_line, ver_line, 'or')
            cell.add(plus_sign)

            # Create the annotation next to the marker
            col_index += 1
            label_text = f"{row_labels[row_index]}{col_index}"
            label = gdspy.Text(
                label_text, 50, position=(x + marker_size, y + marker_size)
            )
            cell.add(label)

# Save the design to a GDS file
lib.write_gds('fiducial_marks.gds')