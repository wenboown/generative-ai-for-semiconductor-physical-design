import gdspy

# Define the layout specifications (in µm)
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0
gate_length = 0.1
sd_length = 0.4
sd_extension = 0.2

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell("FinFET")

# Create the fin (Layer 1)
fin = gdspy.Rectangle((0, -fin_width/2), (fin_length, fin_width/2), layer=1)

# Create the gate (Layer 2)
gate_x = (fin_length - gate_length) / 2
gate = gdspy.Rectangle(
    (gate_x, -fin_height/2 - sd_extension),
    (gate_x + gate_length, fin_height/2 + sd_extension),
    layer=2
)

# Create source and drain regions (Layer 3)
source = gdspy.Rectangle(
    (0, -fin_width/2 - sd_extension),
    (sd_length, fin_width/2 + sd_extension),
    layer=3
)
drain = gdspy.Rectangle(
    (fin_length - sd_length, -fin_width/2 - sd_extension),
    (fin_length, fin_width/2 + sd_extension),
    layer=3
)

# Add all elements to the cell
cell.add(fin)
cell.add(gate)
cell.add(source)
cell.add(drain)

# Save the layout to a GDS file
lib.write_gds("finfet_layout.gds")

# Optional: View the layout