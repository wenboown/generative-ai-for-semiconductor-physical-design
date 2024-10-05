import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("HelloGDS")

# Create the text element
text = gdspy.Text("Hello, GDS!", 5, (0, 0), layer=1)

# Center the text at (0, 0)
text.translate(-text.get_bounding_box().center[0], -text.get_bounding_box().center[1])

# Add the text to the cell
cell.add(text)

# Save the design to a GDS file
lib.write_gds("HelloGDS.gds")