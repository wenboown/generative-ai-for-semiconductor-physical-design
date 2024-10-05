import gdspy
import string

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('CIRCLE_WITH_FIDUCIALS')

# Create the main circle (3.2 mm diameter)
circle = gdspy.Round((0, 0), 1600, tolerance=0.1)
cell.add(circle)

# Define fiducial mark dimensions
fiducial_size = 50  # 50 μm
fiducial_thickness = 5  # 5 μm

# Create fiducial mark
def create_fiducial(x, y):
    horizontal = gdspy.Rectangle((x - fiducial_size/2, y - fiducial_thickness/2),
                                 (x + fiducial_size/2, y + fiducial_thickness/2))
    vertical = gdspy.Rectangle((x - fiducial_thickness/2, y - fiducial_size/2),
                               (x + fiducial_thickness/2, y + fiducial_size/2))
    return gdspy.boolean(horizontal, vertical, 'or')

# Create grid of fiducials
grid_size = 200  # 200 μm spacing
max_radius = 1500  # Slightly less than circle radius to ensure all fiducials are inside

rows = string.ascii_uppercase
col = 1
for x in range(-max_radius, max_radius + 1, grid_size):
    row = 0
    for y in range(-max_radius, max_radius + 1, grid_size):
        if x*x + y*y <= max_radius*max_radius:
            fiducial = create_fiducial(x, y)
            cell.add(fiducial)
            
            # Add annotation
            text = f"{rows[row]}{col}"
            label = gdspy.Text(text, 30, (x + 40, y - 40))
            cell.add(label)
            
            row += 1
    col += 1

# Save the design to a GDS file
lib.write_gds('circle_with_fiducials.gds')

# Optional: View the layout