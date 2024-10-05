import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TRAPEZOID')

# Define the coordinates of the trapezoid
# Upper edge (top base): 10 mm width at y = +4 mm
# Lower edge (bottom base): 20 mm width at y = -4 mm
# Centered at (0, 0)

# Convert dimensions from mm to micrometers (1 mm = 1000 micrometers)
upper_width = 10 * 1000  # in micrometers
lower_width = 20 * 1000  # in micrometers
height = 8 * 1000        # in micrometers
half_height = height / 2

# Calculate the y-coordinates
y_top = half_height
y_bottom = -half_height

# Calculate the x-coordinates for the upper and lower edges
upper_half_width = upper_width / 2
lower_half_width = lower_width / 2

# Define the points of the trapezoid
points = [
    (-upper_half_width, y_top),    # Top left
    (upper_half_width, y_top),     # Top right
    (lower_half_width, y_bottom),  # Bottom right
    (-lower_half_width, y_bottom), # Bottom left
]

# Create the trapezoid polygon
trapezoid = gdspy.Polygon(points, layer=0)

# Add the trapezoid to the cell
cell.add(trapezoid)

# Save the GDSII file
lib.write_gds('trapezoid.gds')