import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Layout')

# Create the rectangle
rect = gdspy.Rectangle((0, 0), (30e3, 10e3), layer=0)

# Add the rectangle to the cell
cell.add(rect)

# Create the text
text = gdspy.Text('IBM Research', size=3e3, position=(15e3, 5e3), layer=1)

# Add the text to the cell
cell.add(text)

# Save the design to a GDS file
lib.write_gds('layout.gds')