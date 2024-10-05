import gdspy
import numpy as np

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('fiducial-mark-layout')

# Define the circle parameters
circle_radius = 3.2  # mm
circle_x = 0
circle_y = 0

# Create the circle
circle = gdspy.Round((circle_x, circle_y), circle_radius, tolerance=0.01)
cell.add(circle)

# Define the fiducial mark parameters
fiducial_size = 200  # um
fiducial_spacing = 200  # um

# Define the annotation font
font = gdspy.TextGenerator('font', size=100,GBL='font')

# Create the fiducial marks and annotations
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(26):  # Assuming 26 fiducials in a 5x5 grid with alphabet A-Z labeling
    row = i // 5
    col = i % 5
    fiducial_x = col * fiducial_spacing - 2 * fiducial_spacing  # Centered at (0,0) 
    fiducial_y = -row * fiducial_spacing + 2 * fiducial_spacing  # Since we start from top left
    # Draw horizontal line
    fiducial_h_line = gdspy.Rectangle((fiducial_x-fiducial_size/2, fiducial_y), (fiducial_x+fiducial_size/2, fiducial_y), 0.1)
    cell.add(fiducial_h_line)
    # Draw vertical line
    fiducial_v_line = gdspy.Rectangle((fiducial_x, fiducial_y-fiducial_size/2), (fiducial_x, fiducial_y+fiducial_size/2), 0.1)
    cell.add(fiducial_v_line)
    # Annotation
    annotation = font.text(f'A{i+1}', (fiducial_x+fiducial_size/2, fiducial_y))
    cell.add(annotation)

# Save the layout to a GDS file
lib.write_gds('fiducial_marks.gds')