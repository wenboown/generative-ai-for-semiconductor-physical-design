import gdspy

# Define the design specifications
arrow_length = 10  # mm
head_width = 2  # mm
body_width = head_width / 3  # mm

# Create a new GDS library
lib = gdspy.GdsLibrary()

# Define the cell for the arrow
cell = lib.new_cell('arrow')

# Create the arrow head
arrow_head = gdspy.Polygon([(arrow_length - head_width/2, -head_width/2), 
                            (arrow_length, 0), 
                            (arrow_length - head_width/2, head_width/2), 
                            (arrow_length - head_width, head_width/2), 
                            (arrow_length - head_width, -head_width/2)])

# Create the arrow body
arrow_body = gdspy.Rectangle(0, -body_width/2, arrow_length - head_width, body_width/2)

# Add the arrow head and body to the cell
cell.add(arrow_head)
cell.add(arrow_body)

# Save the design to a GDS file
lib.write_gds('arrow.gds')