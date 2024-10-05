import gdspy

# Parse the user's design specifications
circle_radius = 3.2  # in mm
fiducial_length = 200  # in um
fiducial_width = fiducial_length
annotate_rows = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
annotate_columns = range(1, 1000)  # assuming 1000 columns max

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('fiducial_circle')

# Create the circle
circle = gdspy.Round((0, 0), circle_radius * 1000, num_points=128)
cell.add(circle)

# Define the fiducial mark dimensions in um
fiducial_half_length = fiducial_length / 2
fiducial_half_width = fiducial_width / 2

# Create the fiducial marks
row_idx = 0
for row in annotate_rows:
    col_idx = 0
    for col in annotate_columns:
        if col_idx * fiducial_length > 2 * circle_radius * 1000:
            break
        x = col_idx * fiducial_length - circle_radius * 1000
        y = row_idx * fiducial_length - circle_radius * 1000

        # Create the "+" fiducial mark
        fiducialMARK = gdspy.Rectangle((x - fiducial_half_length, y - fiducial_half_width),
                                        (x + fiducial_half_length, y + fiducial_half_width),
                                        layer=1)
        cell.add(fiducialMARK)
        fiducialMARK = gdspy.Rectangle((x - fiducial_half_width, y - fiducial_half_length),
                                        (x + fiducial_half_width, y + fiducial_half_length),
                                        layer=1)
        cell.add(fiducialMARK)

        # Add annotations
        text = gdspy.Text(f'{row}{col}', 50, (x, y + fiducial_length))
        cell.add(text)
        col_idx += 1
    row_idx += 1

# Save the design to a GDS file
lib.write_gds('fiducial_circle.gds')