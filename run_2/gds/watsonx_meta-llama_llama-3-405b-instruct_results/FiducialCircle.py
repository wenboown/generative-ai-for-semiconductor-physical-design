import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('fiducial_circle')

# Define the circle parameters
circle_radius = 3.2 / 2  # 3.2 mm / 2 = 1.6 mm = 1600 um
circle_center = (0, 0)

# Create the circle
circle = gdspy.Round(circle_center, circle_radius)
cell.add(circle)

# Define the fiducial mark parameters
fiducial_size = 50  # 50 um
fiducial_spacing = 200  # 200 um
num_fiducials = int(2 * math.pi * circle_radius / fiducial_spacing)

# Create the fiducial marks
for i in range(num_fiducials):
    angle = i * 2 * math.pi / num_fiducials
    x = circle_center[0] + circle_radius * math.cos(angle)
    y = circle_center[1] + circle_radius * math.sin(angle)
    
    # Create the "+" sign
    plus_sign = gdspy.Path(fiducial_size, (x, y))
    plus_sign.segment((x, y + fiducial_size), '+')
    plus_sign.segment((x, y - fiducial_size), '+')
    plus_sign.segment((x + fiducial_size, y), '+')
    plus_sign.segment((x - fiducial_size, y), '+')
    cell.add(plus_sign)
    
    # Add annotations
    row = chr(65 + i // 26)  # 65 is ASCII code for 'A'
    col = i % 26 + 1
    text = f'{row}{col}'
    annotation = gdspy.Text(text, 20, (x + fiducial_size + 10, y))
    cell.add(annotation)

# Save the design to a GDS file
lib.write_gds('fiducial_circle.gds')