import gdspy

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('IBM_Research_Layout')

# Define rectangle dimensions (in micrometers)
width = 30000  # 30 mm = 30000 μm
height = 10000  # 10 mm = 10000 μm

# Create rectangle on layer 0
rectangle = gdspy.Rectangle((0, 0), (width, height), layer=0)

# Create text on layer 1
text = "IBM Research"
text_size = 1000  # Adjust this value to change text size
text_position = (width / 2, height / 2)  # Center of the rectangle

text_elem = gdspy.Text(text, text_size, text_position, layer=1, anchor='cc')  # 'cc' means center-center anchoring

# Add rectangle and text to the cell
cell.add(rectangle)
cell.add(text_elem)

# Save the design to a GDS file
lib.write_gds('ibm_research_layout.gds')

print("GDS file 'ibm_research_layout.gds' has been generated successfully.")