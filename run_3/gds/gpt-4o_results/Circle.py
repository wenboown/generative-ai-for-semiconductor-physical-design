import gdspy

# Create the GDSII library, name it 'circle_design'.
lib = gdspy.GdsLibrary('circle_design')

# Create a cell to hold the design.
cell = lib.new_cell('CIRCLE')

# Define the radius of the circle in micrometers (10 mm = 10000 micrometers).
radius = 10000

# Create a circle with center at (0,0) and the specified radius.
circle = gdspy.Round((0, 0), radius, layer=0)

# Add the circle to the cell.
cell.add(circle)

# Save the library in a GDSII file called 'circle_design.gds'.
lib.write_gds('circle_design.gds')

print("GDSII file 'circle_design.gds' with a circle generated successfully.")