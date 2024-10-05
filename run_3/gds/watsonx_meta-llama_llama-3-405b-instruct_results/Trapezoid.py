import gdspy

def create_trapezoid(lib, cell, center=(0, 0), upper_edge=10, lower_edge=20, height=8):
    x_center, y_center = center
    upper_half_height = height / 2
    points = [
        (x_center - upper_edge / 2, y_center - upper_half_height),
        (x_center + upper_edge / 2, y_center - upper_half_height),
        (x_center + lower_edge / 2, y_center + upper_half_height),
        (x_center - lower_edge / 2, y_center + upper_half_height)
    ]
    trapezoid = gdspy.Polygon(points, layer=1, datatype=0)
    cell.add(trapezoid)

lib = gdspy.GdsLibrary()
cell = lib.new_cell('Trapezoid')
create_trapezoid(lib, cell)
lib.write_gds('trapezoid.gds')