import gdspy
import numpy as np

# Define the design specifications
circle_diameter = 3.2  # mm
fiducial_size = 0.2  # mm
fiducial_spacing = 0.2  # mm
annotation_offset = 0.05  # mm

# Convert design specs to microns
circle_diameter_um = circle_diameter * 1000
fiducial_size_um = fiducial_size * 1000
fiducial_spacing_um = fiducial_spacing * 1000
annotation_offset_um = annotation_offset * 1000

# Create the GDS library and cell
lib = gdspy.GdsLibrary(name='fiducial_circle')
cell = lib.new_cell('fiducial_circle')

# Draw the circle
circle = gdspy.Round(center=(0, 0), radius=circle_diameter_um/2, layer=0, datatype=0)
cell.add(circle)

# Calculate the number of fiducial marks that fit inside the circle
num_fiducials = int(np.floor(np.sqrt(2) * circle_diameter_um / fiducial_spacing_um))

# Draw the fiducial marks and annotations
for i in range(-num_fiducials, num_fiducials+1):
    for j in range(-num_fiducials, num_fiducials+1):
        # Skip the center mark
        if i == 0 and j == 0:
            continue
        
        # Calculate the fiducial mark position
        x = i * fiducial_spacing_um
        y = j * fiducial_spacing_um
        
        # Draw the fiducial mark
        fiducial = gdspy.Polygon([
            (x - fiducial_size_um/2, y - fiducial_size_um/2),
            (x + fiducial_size_um/2, y - fiducial_size_um/2),
            (x + fiducial_size_um/2, y + fiducial_size_um/2),
            (x - fiducial_size_um/2, y + fiducial_size_um/2),
            (x - fiducial_size_um/2, y - fiducial_size_um/2),
            (x, y - fiducial_size_um/2),
            (x, y + fiducial_size_um/2),
            (x - fiducial_size_um/2, y + fiducial_size_um/2),
            (x - fiducial_size_um/2, y - fiducial_size_um/2)
        ], layer=1, datatype=0)
        cell.add(fiducial)
        
        # Add the annotation
        annotation = gdspy.Label(f"{chr(65 + int((i + num_fiducials) / 2))}{int((j + num_fiducials) / 2) + 1}", 
                                 (x + annotation_offset_um, y + annotation_offset_um), 
                                 layer=2, 
                                 texttype=0, 
                                 size=100)
        cell.add(annotation)

# Save the GDS file
lib.write_gds('fiducial_circle.gds')