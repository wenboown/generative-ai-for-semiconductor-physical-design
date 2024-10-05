import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Trapezoid')

# Parse the user’s design specifications
upper_edge = 10  # mm
lower_edge = 20  # mm
height = 8  # mm
center = (0, 0)  # mm

# Calculate the coordinates for the trapezoid
x1 = center[0] - upper_edge / 2
y1 = center[1] + height / 2
x2 = center[0] + upper_edge / 2
y2 = center[1] + height / 2
x3 = center[0] + lower_edge / 2
y3 = center[1] - height / 2
x4 = center[0] - lower_edge / 2
y4 = center[1] - height / 2

# Create the trapezoid polygon with precise coordinates
trap_points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
trapezoid = gdspy.Polygon(trap_points, layer=0, datatype=0)

# Ensure elements are placed correctly and maintain their intended relationships
cell.add(trapezoid)

# Save the design to a GDS file
lib.write_gds('Trapezoid.gds')