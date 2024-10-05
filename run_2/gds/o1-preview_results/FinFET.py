import gdspy

# FinFET dimensions (all units in micrometers)
fin_width = 0.1      # Fin width (into the page, not represented in 2D layout)
fin_height = 0.2     # Fin height (y-direction)
fin_length = 1.0     # Fin length (x-direction)

gate_length = 0.1          # Gate length (along x-axis)
source_drain_length = 0.4  # Source/drain length (along x-axis)
sd_extension = 0.2         # Source/drain extension beyond the fin (along x-axis)

# Layers for different regions
fin_layer = 1
gate_layer = 2
sd_layer = 3

# Create a new GDSII library and add a cell for the FinFET
gdspy.current_library = gdspy.GdsLibrary()
cell = gdspy.Cell('FINFET')

# Define the fin geometry
fin = gdspy.Rectangle(
    (0.0, 0.0),  # Bottom-left corner (x0, y0)
    (fin_length, fin_height),  # Top-right corner (x1, y1)
    layer=fin_layer
)
cell.add(fin)

# Define the source region geometry
source = gdspy.Rectangle(
    (-sd_extension, 0.0),  # Extend beyond fin by sd_extension
    (sd_extension, fin_height),
    layer=sd_layer
)
cell.add(source)

# Define the drain region geometry
drain = gdspy.Rectangle(
    (fin_length - sd_extension, 0.0),
    (fin_length + sd_extension, fin_height),
    layer=sd_layer
)
cell.add(drain)

# Define the gate geometry centered over the fin
gate_start_x = (fin_length - gate_length) / 2
gate_end_x = gate_start_x + gate_length
gate = gdspy.Rectangle(
    (gate_start_x, 0.0),
    (gate_end_x, fin_height),
    layer=gate_layer
)
cell.add(gate)

# Save the design to a GDSII file
gdspy.write_gds('finfet.gds', unit=1.0e-6, precision=1.0e-9)