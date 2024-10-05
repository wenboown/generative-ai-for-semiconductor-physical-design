import gdspy
import string

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('FIDUCIAL_MARKS')

# Create the main circle (3.2 mm diameter)
circle = gdspy.Round((0, 0), 1600, tolerance=0.1)
cell.add(circle)

# Function to create a "+" fiducial mark
def create_fiducial(x, y, size=50):
    horizontal = gdspy.Rectangle((x - size/2, y - size/10), (x + size/2, y + size/10))
    vertical = gdspy.Rectangle((x - size/10, y - size/2), (x + size/10, y + size/2))
    return gdspy.boolean(horizontal, vertical, 'or')

# Calculate the number of markers that fit in the circle
markers_per_side = int(3200 / 200)  # 3200 μm / 200 μm
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
            row = string.ascii_uppercase[j]
            col = str(i + 1)
            text = gdspy.Text(f"{row}{col}", 50, (x + 60, y - 60))
            cell.add(text)

# Save the design to a GDS file
lib.write_gds('fiducial_marks.gds')

# Optional: View the layout