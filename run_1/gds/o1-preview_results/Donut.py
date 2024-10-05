import gdspy

# Create a new GDSII library with units in millimeters
lib = gdspy.GdsLibrary(unit=1e-3, precision=1e-9)

# Create a new cell
cell = lib.new_cell('DONUT')

# Create the donut shape with outer radius 10 mm, inner radius 5 mm, and max point distance 0.01 mm
donut = gdspy.Round((0, 0), 10, inner_radius=5, tolerance=0.01)

# Add the donut to the cell
cell.add(donut)

# Save the library to a GDS file
lib.write_gds('donut.gds')