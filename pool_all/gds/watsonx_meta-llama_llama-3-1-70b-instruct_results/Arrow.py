import gdspy

# Conversion factor from mm to the GDS unit which is usually nm
mm_to_unit = 1e6

# Arrow specifications
arrow_length_mm = 10     # 10 mm long
arrow_head_width_mm = 3  # arbitrary head width
arrow_body_width_mm = arrow_head_width_mm / 3  # body width is 1/3 of the head width

# Convert specifications to GDS units
arrow_length = arrow_length_mm * mm_to_unit
arrow_head_width = arrow_head_width_mm * mm_to_unit
arrow_body_width = arrow_body_width_mm * mm_to_unit

# Define the points for the arrow polygons
points = [
    (0, arrow_body_width / 2),                   # start of body (bottom side)
    (arrow_length - arrow_head_width, arrow_body_width / 2),  # end of body (bottom side before head)

    (arrow_length - arrow_head_width, -arrow_head_width / 2),  # start of head (1)
    (arrow_length, 0),                # tip of the arrow
    (arrow_length - arrow_head_width, arrow_head_width / 2),   # end of head (bottom point)

    (arrow_length - arrow_head_width, arrow_body_width / 2),   # end of body (top side before head)
    (0, arrow_body_width / 2),                   # return to start
    (0, -arrow_body_width / 2),                   # start of body (top side)
    (arrow_length - arrow_head_width, -arrow_body_width / 2),  # end of body (top side before head)
    (arrow_length - arrow_head_width, -arrow_head_width / 2)   # start of head (2)
]

# Create the GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('ARROW')

# Create the arrow polygon
arrow = gdspy.Polygon(points)
cell.add(arrow)

# Save the design to a GDS file
lib.write_gds('arrow_design.gds')

print("Arrow GDS file has been created: arrow_design.gds")