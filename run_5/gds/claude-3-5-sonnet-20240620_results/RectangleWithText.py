import gdspy

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('IBM_Research_Logo')

# Define rectangle dimensions (in micrometers)
width = 30000  # 30 mm
height = 10000  # 10 mm

# Create rectangle on layer 0
rectangle = gdspy.Rectangle((0, 0), (width, height), layer=0)

# Create text on layer 1
text = "IBM Research"
text_size = 1000  # 1 mm height for text

# Calculate center position for text
text_position = (width / 2, height / 2)

# Create text object
text_obj = gdspy.Text(text, text_size, text_position, layer=1, anchor="cc")  # "cc" means center-center

# Add rectangle and text to the cell
cell.add(rectangle)
cell.add(text_obj)

# Save the design to a GDS file
lib.write_gds('ibm_research_logo.gds')

print("GDS file 'ibm_research_logo.gds' has been generated successfully.")