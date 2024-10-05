import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square_design')

# Define the square with precise coordinates
width = 10  # width in mm
square = gdspy.Rectangle((0, 0), (width, width), layer=1)  # lower right corner at 0,0

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_design.gds')