import gdspy

# Conversion factor from mm to micrometers (GDS units)
mm_to_um = 1000

# Arrow specifications
arrow_length_mm = 10    # Arrow length in mm
arrow_head_width_mm = 3 # Head width in mm
arrow_body_width_mm = arrow_head_width_mm / 3 # Body width is 1/3 of the head width

# Convert dimensions to micrometers
arrow_length_um = arrow_length_mm * mm_to_um
arrow_head_width_um = arrow_head_width_mm * mm_to_um
arrow_body_width_um = arrow_body_width_mm * mm_to_um

# Define the arrow shape
arrow_body = gdspy.Rectangle(
    (0, -arrow_body_width_um / 2),
    (arrow_length_um - arrow_head_width_um, arrow_body_width_um / 2)
)

arrow_head = gdspy.Polygon([
    (arrow_length_um - arrow_head_width_um, -arrow_head_width_um / 2),
    (arrow_length_um, 0),
    (arrow_length_um - arrow_head_width_um, arrow_head_width_um / 2)
])

# Create a new GDSII library and a cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('ARROW')

# Add the arrow components to the cell
cell.add(arrow_body)
cell.add(arrow_head)

# Save the design to a GDSII file
lib.write_gds('arrow.gds')

print("Arrow GDS file has been generated: arrow.gds")