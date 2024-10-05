import gdspy
import math

# Create a new GDSII library, which will contain your design
lib = gdspy.GdsLibrary()

# Create a new cell (or layer) to add elements to
cell = lib.new_cell('PENTAGON')

# Define the side length of the pentagon in millimeters
side_length_mm = 10.0
side_length_um = side_length_mm * 1000.0  # Convert to micrometers

# Calculate the radius of the circumscribed circle (in micrometers)
r_um = (side_length_um) / (2 * math.sin(math.pi / 5))

# Initial angle (starting from the top vertex)
theta0 = math.pi / 2  # 90 degrees in radians

# Calculate the angles for each of the five vertices
angles = [theta0 + i * (2 * math.pi / 5) for i in range(5)]

# Calculate the coordinates of each vertex
vertices = [(r_um * math.cos(angle), r_um * math.sin(angle)) for angle in angles]

# Create a polygon with the calculated vertices
pentagon = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(pentagon)

# Save the library into a GDSII file
lib.write_gds('pentagon.gds')

# Optionally, view the layout using gdspy's built-in viewer (commented out)