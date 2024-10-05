import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("Circle_with_Fiducials")

# Define the circle parameters
circle_radius = 3.2  # in mm
circle_center = (0, 0)

# Convert circle radius from mm to um
circle_radius_um = circle_radius * 1000

# Create the circle
circle = gdspy.Round(circle_center, circle_radius_um, tolerance=0.001)
cell.add(circle)

# Define the fiducial mark parameters
fiducial_size = 200  # in um
fiducial_spacing = 200  # in um
fiducial_row_start = ord('A')
fiducial_col_start = 1

# Create the fiducial marks and annotations
for row in range(4):
    for col in range(4):
        fiducial_center = (
            (col - 1) * fiducial_spacing,
            (row - 1) * fiducial_spacing
        )
        
        # Create the fiducial mark
        fiducial_cross = gdspy.Cross(
            fiducial_center,
            size=fiducial_size,
            linewidth=5
        )
        cell.add(fiducial_cross)
        
        # Create the annotation
        annotation_text = f"{chr(fiducial_row_start + row)}{fiducial_col_start + col}"
        annotation = gdspy.Text(
            annotation_text,
            20,
            fiducial_center,
            layer=0
        )
        cell.add(annotation)

# Save the design to a GDS file
lib.write_gds("circle_with_fiducials.gds")