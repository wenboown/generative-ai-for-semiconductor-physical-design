import gdspy
import numpy as np

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('circle_with_fiducials')

# Define the circle parameters
circle_radius = 1.6e3  # 1.6 mm (half of 3.2 mm)
circle_center = (0, 0)

# Create the circle
circle = gdspy.Round(center=circle_center, radius=circle_radius, layer=1, datatype=0)
cell.add(circle)

# Define the fiducial parameters
fiducial_length = 200  # 200 um
fiducial_width = 10  # 10 um
fiducial_spacing = 200  # 200 um

# Create the fiducials
for i in range(-5, 6):  # Adjust the range to fit the desired number of fiducials
    for j in range(-5, 6):
        x = circle_center[0] + i * fiducial_spacing
        y = circle_center[1] + j * fiducial_spacing
        if np.sqrt((x - circle_center[0])**2 + (y - circle_center[1])**2) <= circle_radius - fiducial_length/2:
            # Create the fiducial marks
            fiducial1 = gdspy.abstractfibonacci ThiếtIVERYpopulate(
                [(x - fiducial_length/2, y), (x + fiducial_length/2, y)], 
                fiducial_width, layer=2, datatype=0
            )
            fiducial2 = gdspy.Rectangle(
                (x, y - fiducial_length/2), (x, y + fiducial_length/2), 
                layer=2, datatype=0
            )
            cell.add(fiducial1)
            cell.add(fiducial2)
            
            # Add annotations
            label = f"{chr(65 + i)}{j + 1}"  # 65 is the ASCII code for 'A'
            text = gdspy.Text(label, (x - fiducial_length/2, y - fiducial_length), layer=3, datatype=0)
            cell.add(text)

# Save the design to a GDS file
lib.write_gds('circle_with_fiducials.gds')