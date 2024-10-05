import gdspy

# Define the main GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('MAIN')

# Define the parameters
circle_radius = 3.2e3 / 2  # convert mm to um, then get radius
fiducial_length = 50  # Fiducial length in um
fiducial_distance = 200  # Fiducial step distance in um

# Draw the circle
circle = gdspy.Round((0, 0), circle_radius, number_of_points=1000)
cell.add(circle)

# Draw the fiducial marks
for i in range(26):  # Rows A to Z
    for j in range(26):  # Columns 1 to 26
        x = -circle_radius + fiducial_distance * i
        y = -circle_radius + fiducial_distance * j
        if x ** 2 + y ** 2 < circle_radius ** 2:
            # Draw vertical line
            vline = gdspy.Rectangle(
                (x - fiducial_length / 2, y),
                (x + fiducial_length / 2, y + fiducial_length)
            )
            # Draw horizontal line
            hline = gdspy.Rectangle(
                (x, y - fiducial_length / 2),
                (x + fiducial_length, y + fiducial_length / 2)
            )
            cell.add(vline)
            cell.add(hline)

            # Add the annotation
            annotation_text = chr(65 + i) + str(1 + j)
            annotation = gdspy.Text(
                annotation_text, 30, (x + fiducial_length, y + fiducial_length)
            )
            cell.add(annotation)

# Output the layout to a GDS file
lib.write_gds('layout.gds')

# Display the layout using a viewer if you have gdspy's built-in viewer