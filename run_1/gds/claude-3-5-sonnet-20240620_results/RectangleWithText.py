import gdspy

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('MAIN')

# Create the rectangle (30x10 mm) on layer 0
rectangle = gdspy.Rectangle((0, 0), (30000, 10000), layer=0)

# Create the text "IBM Research" at the center of the rectangle on layer 1
text = gdspy.Text("IBM Research", 500, (15000, 5000), layer=1, anchor="cc")

# Add both elements to the cell
cell.add(rectangle)
cell.add(text)

# Save the design to a GDS file
lib.write_gds('ibm_research_layout.gds')

print("GDS file 'ibm_research_layout.gds' has been created successfully.")