import gdspy
import string

# Create a new library
lib = gdspy.GdsLibrary()

# Create the main cell
cell = lib.new_cell('MAIN')

# Create the 3.2 mm circle
circle = gdspy.Round((0, 0), 1600)  # Radius is 1600 µm (3200 µm diameter)
cell.add(circle)

# Define fiducial mark dimensions
fiducial_size = 50  # 50 µm for each arm of the "+" sign

# Create fiducial mark as a "+" sign
fiducial = gdspy.CrossSection(
    width=fiducial_size/5,
    layer=1,
    sections=[[fiducial_size, "+x"], [fiducial_size, "+y"], [fiducial_size, "-x"], [fiducial_size, "-y"]]
)

# Calculate the number of markers that fit within the circle
markers_per_side = int(3200 / 200)  # 3200 µm / 200 µm spacing
start_coord = -1500  # Start slightly off-center to center the grid

# Create fiducial marks and annotations
for i in range(markers_per_side):
    for j in range(markers_per_side):
        x = start_coord + i * 200
        y = start_coord + j * 200
        
        # Only place markers inside the circle
        if x**2 + y**2 <= 1600**2:
            cell.add(gdspy.CellReference(fiducial, (x, y)))
            
            # Add annotations
            row_label = string.ascii_uppercase[i % 26]
            col_label = str(j + 1)
            annotation = f"{row_label}{col_label}"
            
            text = gdspy.Text(annotation, 30, (x + 60, y - 60), layer=2)
            cell.add(text)

# Save the GDS file
lib.write_gds('fiducial_circle.gds')

# Optional: View the layout