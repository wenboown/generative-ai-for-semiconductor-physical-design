import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('ARROW')

# Create the arrow body
body = gdspy.Rectangle((0, -1/3), (7.5, 1/3))

# Create the arrow head
head = gdspy.Polygon([(7.5, -1), (10, 0), (7.5, 1)])

# Add the body and head to the cell
cell.add(body)
cell.add(head)

# Save the design to a GDS file
lib.write_gds('arrow.gds')

# Optional: View the layout