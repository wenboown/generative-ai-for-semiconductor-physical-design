import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MICROFLUIDIC_CHIP')

# Layer definitions
BULK_LAYER = 0
VIA_LAYER = 2
CHANNEL_LAYER = 3

# Chip dimensions
chip_width = 30000  # 30 mm in um
chip_height = 20000  # 20 mm in um

# Via specifications
via_radius = 2000  # 2 mm in um
via_spacing = 20000  # 20 mm in um

# Channel specifications
channel_width = 1000  # 1 mm in um

# 1. Draw the chip bulk (layer 0)
bulk = gdspy.Rectangle((0, 0), (chip_width, chip_height), layer=BULK_LAYER)
cell.add(bulk)

# 2. Draw the two circular vias (layer 2)
via1_center = (chip_width/2 - via_spacing/2, chip_height/2)
via2_center = (chip_width/2 + via_spacing/2, chip_height/2)

via1 = gdspy.Round(via1_center, via_radius, layer=VIA_LAYER)
via2 = gdspy.Round(via2_center, via_radius, layer=VIA_LAYER)
cell.add(via1)
cell.add(via2)

# 3. Draw the rectangular channel connecting the vias (layer 3)
channel_path = gdspy.Path(channel_width, via1_center, layer=CHANNEL_LAYER)
channel_path.segment(via_spacing, '+x')
cell.add(channel_path)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')

# Optional: View the layout