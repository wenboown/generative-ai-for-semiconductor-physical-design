import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('IBM_Research_Layout')

# Define rectangle dimensions (in micrometers)
width = 30000  # 30 mm
height = 10000  # 10 mm

# Create rectangle on layer 0
rectangle = gdspy.Rectangle((0, 0), (width, height), layer=0)

# Calculate center of the rectangle
center_x = width / 2
center_y = height / 2

# Create text at the center of the rectangle on layer 1
text = gdspy.Text("IBM Research", 500, (center_x, center_y), layer=1, anchor="cc")

# Add rectangle and text to the cell
cell.add(rectangle)
cell.add(text)

# Save the GDS file
lib.write_gds('ibm_research_layout.gds')

print("GDS file 'ibm_research_layout.gds' has been generated successfully.")