import gdspy
import string

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('CIRCLE_WITH_FIDUCIALS')

# Create the main circle (3.2 mm diameter)
circle = gdspy.Round((0, 0), 1600)
cell.add(circle)

# Function to create a "+" fiducial mark
def create_fiducial(x, y):
    horizontal = gdspy.Rectangle((x - 100, y - 10), (x + 100, y + 10))
    vertical = gdspy.Rectangle((x - 10, y - 100), (x + 10, y + 100))
    return gdspy.boolean(horizontal, vertical, 'or')

# Calculate the number of markers that fit in the circle
markers_per_side = int(3200 / 200)  # 3200 um / 200 um
start = -markers_per_side * 100  # Start from the edge

# Create fiducial marks and annotations
for i in range(markers_per_side * 2 + 1):
    for j in range(markers_per_side * 2 + 1):
        x = start + i * 200
        y = start + j * 200

        # Check if the marker is inside the circle
        if x**2 + y**2 <= 1600**2:
            cell.add(create_fiducial(x, y))

            # Add annotation
            row = string.ascii_uppercase[j % 26]
            col = str(i % 26 + 1)
            text = gdspy.Text(f"{row}{col}", 50, (x + 60, y - 60))
            cell.add(text)

# Save the design to a GDS file
lib.write_gds('circle_with_fiducials.gds')