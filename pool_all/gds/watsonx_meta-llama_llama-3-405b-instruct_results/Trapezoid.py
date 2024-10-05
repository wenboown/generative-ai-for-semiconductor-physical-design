import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('TRAPEZOID')

# Define the dimensions in micrometers
upper_edge = 10e3  # 10 mm in micrometers
lower_edge = 20e3  # 20 mm in micrometers
height = 8e3      # 8 mm in micrometers

# Calculate the coordinates of the trapezoid vertices
x1 = -lower_edge / 2
x2 = lower_edge / 2
x3 = upper_edge / 2
x4 = -upper_edge / 2
y1 = -height / 2
y2 = height / 2

# Create the trapezoid as a polygon
vertices = [(x1, y1), (x2, y1), (x3, y2), (x4, y2)]
trapezoid = gdspy.Polygon(vertices, layer=0)

# Add the trapezoid to the cell
cell.add(trapezoid)

# Save the design to a GDS file
lib.write_gds('trapezoid.gds')