import gdspy

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('FIDUCIAL_MARKERS')

# Define circle parameters
radius = 1600  # um (since diameter is 3.2 mm)
circle = gdspy.Round((0, 0), radius)
cell.add(circle)

# Define grid parameters
spacing = 200  # um
positions = list(range(-1600, 1601, spacing))  # positions from -1600 um to +1600 um

# Generate the fiducial marks and annotations
num_rows = len(positions)
num_cols = len(positions)

# Create row labels from 'A' onward
row_labels = [chr(ord('A') + i) for i in range(num_rows)]
# Reverse row labels so that topmost row is 'A'
row_labels = row_labels[::-1]

# Create column labels starting from '1'
column_labels = [str(i + 1) for i in range(num_cols)]

for i, y in enumerate(positions):
    for j, x in enumerate(positions):
        # Check if the point is inside the circle
        if x**2 + y**2 <= radius**2:
            # Draw the '+' sign at (x, y)
            plus_size = 50  # um (half length of each arm)
            # Horizontal line of '+'
            h_line = gdspy.Rectangle((x - plus_size, y - 1), (x + plus_size, y + 1))
            # Vertical line of '+'
            v_line = gdspy.Rectangle((x - 1, y - plus_size), (x + 1, y + plus_size))
            cell.add([h_line, v_line])
            
            # Add annotations next to each marker
            # Place the text slightly offset from the marker
            text_offset = 20  # um
            row_label = row_labels[i]
            column_label = column_labels[j]
            annotation_text = f'{row_label}{column_label}'
            annotation = gdspy.Text(annotation_text, 30, (x + plus_size + text_offset, y + plus_size + text_offset))
            cell.add(annotation)

# Save the GDS file
lib.write_gds('fiducial_markers.gds')