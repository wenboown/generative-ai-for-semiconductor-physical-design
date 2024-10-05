import gdspy
import string

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell
cell = lib.new_cell('Fiducial_Marks')

# Draw the circle with radius 1600 μm (1.6 mm)
radius = 1600  # in μm
circle = gdspy.Round((0, 0), radius, layer=0)
cell.add(circle)

# Generate position grid
spacing = 200  # 200 μm apart
num_positions = int((2 * radius) / spacing) + 1  # Total number of positions along one axis
positions = [(-radius + i * spacing) for i in range(num_positions)]  # Positions from -1600 μm to +1600 μm

# Row labels from 'A' onwards
row_labels = list(string.ascii_uppercase)

# Iterate over grid positions
for j, y in enumerate(positions):
    for i, x in enumerate(positions):
        # Check if the point is inside the circle
        if x**2 + y**2 <= radius**2:
            # Define parameters for the '+' sign
            arm_length = 50  # Length of each arm of the '+', in μm
            arm_width = 10   # Width of each arm, in μm

            # Create the vertical arm of the '+'
            rect_vertical = gdspy.Rectangle(
                (x - arm_width / 2, y - arm_length / 2),
                (x + arm_width / 2, y + arm_length / 2),
                layer=0
            )

            # Create the horizontal arm of the '+'
            rect_horizontal = gdspy.Rectangle(
                (x - arm_length / 2, y - arm_width / 2),
                (x + arm_length / 2, y + arm_width / 2),
                layer=0
            )

            # Combine both arms to form the '+' sign
            cross = gdspy.boolean(rect_vertical, rect_horizontal, 'or', layer=0)
            cell.add(cross)

            # Assign row labels (A-Z)
            if j < len(row_labels):
                row_label = row_labels[j]
            else:
                # For rows beyond 'Z', use double letters
                row_label = row_labels[j // 26 - 1] + row_labels[j % 26]

            # Assign column labels starting from 1
            column_label = str(i + 1)

            # Create the annotation text
            annotation = f'Row: {row_label}, Column: {column_label}'

            # Position the label next to the marker
            label_x = x + arm_length
            label_y = y + arm_length

            # Add the label to the cell
            label = gdspy.Label(
                annotation,
                position=(label_x, label_y),
                anchor='nw',  # Position label relative to the northwest corner
                layer=1
            )
            cell.add(label)

# Save the design to a GDSII file
lib.write_gds('fiducial_marks.gds')