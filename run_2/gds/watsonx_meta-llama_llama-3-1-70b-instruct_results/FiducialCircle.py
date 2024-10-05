import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("fiducial_circle")

# Define the circle parameters
circle_radius = 3200  # microns

# Create the circle
circle = gdspy.Round(
    (0, 0),  # center coordinates
    circle_radius,
    tolerance=0.001,
    max_points=100,
    layer=1,
    datatype=0,
)
cell.add(circle)

# Define the fiducial mark parameters
fiducial_length = 200  # microns
fiducial_width = 200  # microns
fiducial_spacing = 200  # microns

# Define the annotation parameters
annotation_font = "Arial"
annotation_size = 100  # microns

# Create the fiducial marks and annotations
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(26):
    row = alpha[i]
    for j in range(13):
        column = str(j + 1)
        x = -1600 + j * fiducial_spacing
        y = 800 - i * fiducial_spacing

        # Create the fiducial mark
        fiducial = gdspy.Polygon([
            (x - fiducial_length / 2, y),
            (x + fiducial_length / 2, y),
            (x, y - fiducial_length / 2),
            (x, y + fiducial_length / 2),
        ], layer=2, datatype=0)
        cell.add(fiducial)

        # Create the annotation
        annotation = gdspy.Text(
            f"{row}{column}",
            x=x + fiducial_length / 2 + 50,
            y=y,
            font=annotation_font,
            size=annotation_size,
            layer=3,
            datatype=0,
        )
        cell.add(annotation)

        # Create the fiducial mark for the second half of the column
        fiducial = gdspy.Polygon([
            (x - fiducial_length / 2, y),
            (x + fiducial_length / 2, y),
            (x, y - fiducial_length / 2),
            (x, y + fiducial_length / 2),
        ], layer=2, datatype=0)
        cell.add(gdspy.Translate(fiducial, (0, -1600)))

        # Create the annotation for the second half of the column
        annotation = gdspy.Text(
            f"{row}{column}",
            x=x + fiducial_length / 2 + 50,
            y=y - 1600,
            font=annotation_font,
            size=annotation_size,
            layer=3,
            datatype=0,
        )
        cell.add(annotation)

# Save the GDS file
lib.write_gds("fiducial_circle.gds")