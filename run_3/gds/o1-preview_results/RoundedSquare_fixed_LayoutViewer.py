import gdspy
import numpy as np

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('ROUNDED_SQUARE')

# Parameters for the square and rounding
width = 10.0        # Width of the square in mm
height = 10.0       # Height of the square in mm
radius = 1.0        # Radius of the rounded corners in mm

# Coordinates for the square boundaries
x0, y0 = 0.0, 0.0                   # Bottom-left corner
x1, y1 = x0 + width, y0 + height    # Top-right corner

# Number of points to approximate each corner arc
points_per_quadrant = 16

# Function to create a rounded rectangle polygon
def create_rounded_rectangle(x0, y0, x1, y1, radius, points_per_quadrant):
    # Ensure the radius is not larger than half the width or height
    radius = min(radius, abs(x1 - x0) / 2, abs(y1 - y0) / 2)

    # Define corner centers
    bl_center = (x0 + radius, y0 + radius)  # Bottom-left
    br_center = (x1 - radius, y0 + radius)  # Bottom-right
    tr_center = (x1 - radius, y1 - radius)  # Top-right
    tl_center = (x0 + radius, y1 - radius)  # Top-left

    # Angles for arcs (in radians)
    angle_range = np.linspace(0, np.pi / 2, points_per_quadrant)

    # Bottom-left corner arc
    bl_arc = [
        (
            bl_center[0] - radius * np.cos(angle),
            bl_center[1] - radius * np.sin(angle)
        )
        for angle in np.linspace(np.pi, 1.5 * np.pi, points_per_quadrant)
    ]

    # Bottom edge
    bottom_edge = [(bl_arc[0][0], y0), (br_center[0], y0)]

    # Bottom-right corner arc
    br_arc = [
        (
            br_center[0] + radius * np.cos(angle),
            br_center[1] - radius * np.sin(angle)
        )
        for angle in np.linspace(1.5 * np.pi, 2 * np.pi, points_per_quadrant)
    ]

    # Right edge
    right_edge = [(x1, br_arc[-1][1]), (x1, tr_center[1])]

    # Top-right corner arc
    tr_arc = [
        (
            tr_center[0] + radius * np.cos(angle),
            tr_center[1] + radius * np.sin(angle)
        )
        for angle in angle_range
    ]

    # Top edge
    top_edge = [(tr_arc[-1][0], y1), (tl_center[0], y1)]

    # Top-left corner arc
    tl_arc = [
        (
            tl_center[0] - radius * np.cos(angle),
            tl_center[1] + radius * np.sin(angle)
        )
        for angle in np.linspace(0.5 * np.pi, np.pi, points_per_quadrant)
    ]

    # Left edge
    left_edge = [(x0, tl_arc[-1][1]), (x0, bl_center[1])]

    # Combine all points
    points = (
        bl_arc + bottom_edge +
        br_arc + right_edge +
        tr_arc + top_edge +
        tl_arc + left_edge
    )

    return gdspy.Polygon(points)

# Create the rounded square
rounded_square = create_rounded_rectangle(
    x0, y0, x1, y1, radius, points_per_quadrant
)

# Add the polygon to the cell
cell.add(rounded_square)

# Save the design to a GDSII file
lib.write_gds('rounded_square.gds')

# Optional: View the layout using the internal viewer (requires a GUI)
pip install gdspy