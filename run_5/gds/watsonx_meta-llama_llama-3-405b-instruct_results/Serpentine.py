import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('serpentine')

# Define the path width, number of turns, segment length, and layer/datatype
path_width = 1  # in µm
num_turns = 15
segment_length = 50  # in µm
layer = 2
datatype = 6

# Initialize the current position
x, y = 0, 0

# Generate the serpentine pattern
for i in range(num_turns):
    if i % 2 == 0:  # horizontal segments
        cell.add(gdspy.Rectangle((x, y), (x + segment_length, y + path_width), layer=layer, datatype=datatype))
        x += segment_length
    else:  # vertical segments
        cell.add(gdspy.Rectangle((x - path_width, y), (x, y + segment_length), layer=layer, datatype=datatype))
        y += segment_length

# Save the design to a GDS file
lib.write_gds('serpentine.gds')