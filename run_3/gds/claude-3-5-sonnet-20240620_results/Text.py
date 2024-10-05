import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TEXT_CELL')

# Create the text
text = gdspy.Text("Hello, GDS!", 5, (0, 0), layer=1, anchor='cc')

# Add the text to the cell
cell.add(text)

# Save the library to a GDS file
lib.write_gds('hello_gds.gds')

print("GDS file 'hello_gds.gds' has been generated.")