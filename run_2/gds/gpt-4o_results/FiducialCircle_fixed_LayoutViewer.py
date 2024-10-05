import gdspy

# Constants and parameters
circle_radius = 3.2e3 / 2  # Radius in microns (3.2 mm divided by 2)
marker_width = 200  # Width of each line in the "+" mark in microns
fiducial_gap = 200  # Gap between fiducial marks in microns
font_size = 140  # Font size for annotations
annotations = [("A" + str(i + 1)) for i in range(26)]  # Generating annotations A1 - A26

def create_fiducial_marks(cell, center, gap, width, labels):
    for idx, label in enumerate(labels):
        x_offset = (idx % 13) * gap - (6 * gap)  # 0 to 12, centered around origin
        y_offset = (idx // 13) * gap - (gap // 2)  # 0 to 1, centered around origin

        # Create the "+" sign
        line_h = gdspy.Rectangle(
            (center[0] + x_offset - width / 2, center[1] + y_offset),
            (center[0] + x_offset + width / 2, center[1] + y_offset + width)
        )
        line_v = gdspy.Rectangle(
            (center[0] + x_offset, center[1] + y_offset - width / 2),
            (center[0] + x_offset + width, center[1] + y_offset + width / 2)
        )
        cell.add(line_h)
        cell.add(line_v)

        # Add the annotation
        label_text = gdspy.Text(
            label, font_size, (center[0] + x_offset + width, center[1] + y_offset - width / 2)
        )
        cell.add(label_text)

# Initialize the GDS Library and Layout Cell
gds_lib = gdspy.GdsLibrary()
layout_cell = gds_lib.new_cell('CIRCLE_WITH_FIDUCIALS')

# Create the main circle
circle = gdspy.Round((0, 0), circle_radius)
layout_cell.add(circle)

# Add fiducial marks with annotations
create_fiducial_marks(layout_cell, (0,0), fiducial_gap, marker_width, annotations)

# Save the design to a GDS file
gds_lib.write_gds('circle_with_fiducials.gds')

# Optionally, if you use an environment that directly supports visualization (like Jupyter):