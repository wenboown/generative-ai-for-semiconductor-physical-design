import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('oval_design')

# Define the oval with precise coordinates
oval = gdspy.Round(
    (0, 0),  # center
    10,      # horizontal radius (half of major axis)
    6.5,     # vertical radius (half of minor axis)
    layer=0, # layer number
    number_of_points=100 # default is 32, increased for smoother curve
)

# Add the oval to the cell
cell.add(oval)

# Save the design to a GDS file
lib.write_gds('oval_design.gds')