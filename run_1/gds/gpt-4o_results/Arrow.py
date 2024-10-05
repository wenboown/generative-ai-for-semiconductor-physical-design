import gdspy

# Define the arrow dimensions
arrow_length = 10  # in mm
arrow_head_width = 3  # in mm
arrow_body_width = arrow_head_width / 3  # 1/3 of the head width

# Convert dimensions to micrometers (since GDSII typically works with micrometers)
arrow_length_um = arrow_length * 1000
arrow_head_width_um = arrow_head_width * 1000
arrow_body_width_um = arrow_body_width * 1000

# Define key points for the arrow shape
# Start point is (0, 0)
start_point = (0, 0)
end_point = (arrow_length_um, 0)
head_right = (arrow_length_um, arrow_head_width_um / 2)
head_left = (arrow_length_um, -arrow_head_width_um / 2)
body_top_right = (2 / 3 * arrow_length_um, arrow_body_width_um / 2)
body_bottom_right = (2 / 3 * arrow_length_um, -arrow_body_width_um / 2)
body_top_left = (start_point[0], arrow_body_width_um / 2)
body_bottom_left = (start_point[0], -arrow_body_width_um / 2)

# Create the arrow using gdspy
arrow_polygon = gdspy.Polygon([
    start_point,
    body_top_right,
    head_left,
    head_right,
    body_bottom_right,
    body_bottom_left,
    start_point
])

# Create a GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('ARROW')

# Add the arrow polygon to the cell
cell.add(arrow_polygon)

# Save the layout to a GDS file
lib.write_gds('arrow.gds')

print("Arrow GDS file has been generated.")