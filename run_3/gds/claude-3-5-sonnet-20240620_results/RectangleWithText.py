import gdspy

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('IBM_Research_Layout')

# Define rectangle dimensions (in micrometers)
width = 30000  # 30 mm
height = 10000  # 10 mm

# Create rectangle on layer 0
rectangle = gdspy.Rectangle((0, 0), (width, height), layer=0)

# Create text on layer 1
text = "IBM Research"
text_height = 1000  # 1 mm tall letters
text_object = gdspy.Text(text, text_height, (width/2, height/2), layer=1, anchor="cc")

# Add rectangle and text to the cell
cell.add(rectangle)
cell.add(text_object)

# Save the design to a GDS file
lib.write_gds('ibm_research_layout.gds')

print("GDS file 'ibm_research_layout.gds' has been generated successfully.")