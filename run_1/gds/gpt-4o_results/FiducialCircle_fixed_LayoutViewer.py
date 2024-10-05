import gdspy

# Define the GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for the design
cell = lib.new_cell('CIRCLE_WITH_FIDUCIALS')

# Circle parameters
circle_radius = 3.2 / 2  # Radius in mm
circle_center = (0, 0)  # Circle centered at origin

# Define the circle
circle = gdspy.Round(circle_center, circle_radius * 1000)  # Convert radius to um for gdspy
cell.add(circle)

# Fiducial parameters
fiducial_spacer = 200  # Spacing in um
fiducial_length = 100  # Length of each line in um
fiducial_width = 10    # Width of each line in um

# Number of fiducial rows and columns
num_rows = 26  # A to Z
num_columns = 10  # Starting from 1 to 10

# Loop through and place each fiducial mark with annotations
for row in range(num_rows):
    for col in range(num_columns):
        # Calculate the center position for the current fiducial mark
        fiducial_center_x = (col - (num_columns - 1) / 2) * fiducial_spacer
        fiducial_center_y = ((num_rows - 1) / 2 - row) * fiducial_spacer
        
        # Create the horizontal line of the "+"
        horizontal_rect = gdspy.Rectangle(
            (fiducial_center_x - fiducial_length / 2, fiducial_center_y - fiducial_width / 2),
            (fiducial_center_x + fiducial_length / 2, fiducial_center_y + fiducial_width / 2)
        )
        
        # Create the vertical line of the "+"
        vertical_rect = gdspy.Rectangle(
            (fiducial_center_x - fiducial_width / 2, fiducial_center_y - fiducial_length / 2),
            (fiducial_center_x + fiducial_width / 2, fiducial_center_y + fiducial_length / 2)
        )
        
        # Add the fiducial marks to the cell
        cell.add(horizontal_rect)
        cell.add(vertical_rect)
        
        # Add the annotation text next to the fiducial mark
        text = gdspy.Text(f'{chr(65 + row)}{col + 1}', 50,
                          (fiducial_center_x + fiducial_length / 2 + 50,
                          fiducial_center_y + fiducial_width / 2 + 50))
        cell.add(text)

# Save the library to a GDS file
lib.write_gds('circle_with_fiducials.gds')

# Optionally, you can view the layout using a gdspy internal viewer if needed